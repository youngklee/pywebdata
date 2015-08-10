import copy
import json
import requests
from xml.etree import ElementTree as ET

from parameter import Input, Output

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
        inputs = {name: obj.value for name, obj in self.get_inputs().items()}
        return self.url.substitute(inputs)
    
    def query(self, **kwargs):
        self.update_parameters(**kwargs)
        url = self.convert_url()
        r = requests.get(url)
        results = output_parsers.get('json', lambda x:x)(r.text)
        print self.parse_results(results)

    def parse_results(self, results):
        return map(self.parse_row, self.f_iter(results))

    def parse_row(self, row):
        result_row = {}
        for name, output in self.get_outputs().items():
            result_row[name] = getattr(self, name).f_parse(row)
        return result_row

    def filter(self, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def get_inputs(cls):
        return cls.get_params(Input)

    @classmethod
    def get_outputs(cls):
        return cls.get_params(Output)

    @classmethod
    def get_params(cls, param_type):
        param_dict = {}
        for name, obj in cls.__dict__.items():
            if isinstance(obj, param_type):
                param_dict[name] = obj
        return param_dict

    @staticmethod
    def f_iter(x):
        return x

    def copy(self):
        return copy.deepcopy(self)