import copy
import json
import requests
from string import Template
from itertools import product, imap
from xml.etree import ElementTree as ET

from parameter import Input, Output
from parsers import parse_query

output_parsers = {'json': json.loads, 'xml': ET.parse}

class ServiceMount(type):

    def __init__(self, name, bases, attrs):
        if not hasattr(self, 'services'):
            self.services = {}
        else:
            self.services[self.name] = self

class BaseService(object):

    __metaclass__ = ServiceMount

    def update_parameters(self, **kwargs):
        for param_name, param_value in kwargs.items():
            getattr(self, param_name).update(param_value)

    def convert_url(self):
        inputs = self.get_input_values()
        return self.url.substitute(inputs)
    
    def query(self, param_dict={}, **kwargs):
        
        if param_dict:
            self.update_parameters(**param_dict)
        else:
            self.update_parameters(**kwargs)

        url = self.convert_url()
        r = requests.get(url)
        results = output_parsers.get('json', lambda x:x)(r.text)

        return  self.parse_results(results)

    def query_many(self, dict_list=[]):
        results = []
        for d in dict_list:
            res = self.query(d)
            results.extend(res)
        return results

    def conditional_query(self, qry_string=None):
        inputs = self.get_inputs()
        conditions = parse_query(qry_string)

        def attach_input_name(qry):
            return dict(zip(inputs.keys(), qry))

        get_input_range = lambda (x, y): y.get_range(conditions[x])
        input_ranges = map(get_input_range, inputs.items())
        queries = imap(attach_input_name, product(*input_ranges))

        return self.query_many(queries)
    
    def parse_results(self, results):
        parser = self.get_parser()
        return map(self.parse_row, parser(results))

    def parse_row(self, row):
        result_row = {}
        for name, output in self.get_outputs().items():
            if getattr(self, name).f_parse:
                result_row[name] = getattr(self, name).f_parse(row)
            else:
                result_row[name] = row.get(name)
        return result_row

    def filter(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def add_url(cls, url):
        setattr(cls, 'url', Template(url))
    
    @classmethod
    def add_input(cls, name, iotype, required=True, min=None, max=None, default=None, incr=None):
        _input = Input(iotype, required, min, max, default, incr)
        setattr(cls, name, _input)
    
    @classmethod
    def add_output(cls, name, iotype):
        _output = Output(iotype)
        setattr(cls, name, _output)
    
    @classmethod
    def add_parser(cls, parse_func):
        setattr(cls, 'parser', parse_func)
    
    @classmethod
    def get_parser(cls):
        return getattr(cls, 'parser')
    
    @classmethod
    def get_inputs(cls):
        return cls.get_params(Input)

    @classmethod
    def get_outputs(cls):
        return cls.get_params(Output)

    @classmethod
    def get_params(cls, param_type, f=lambda x:x):
        param_dict = {}
        for name, obj in cls.__dict__.items():
            if isinstance(obj, param_type):
                param_dict[name] = f(obj)
        return param_dict

    @classmethod
    def get_input_values(cls):
        return cls.get_params(Input, lambda x:x.value)

    @classmethod
    def get_output_values(cls):
        return cls.get_params(Output, lambda x:x.value)

    def copy(self):
        return copy.deepcopy(self)