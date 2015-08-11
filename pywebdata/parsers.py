import re
import operator
from collections import defaultdict

#borrowed from standard library distutils.versionpredicate
compmap = {
    "<": operator.lt, 
    "<=": operator.le, 
    "=": operator.eq,
    ">": operator.gt, 
    ">=": operator.ge, 
    "!=": operator.ne
}

labels = ['name', 'operator', 'value']
condition_splitter = re.compile(r'\s*(\D\w*)\s*(<=|>=|<|>|!=|=)\s*(\d*\.*\d*)')

def parse_query(qry):
    
    def make_cond_dict(cond):
        split_cond = condition_splitter.match(cond).groups()
        d = {}
        d['name'] = split_cond[0]
        d['operator'] = compmap[split_cond[1]]
        d['value'] = split_cond[2]
        return d
        
    conditions = map(make_cond_dict, qry.split('and'))
    conditions_by_name = defaultdict(list)
    for c in conditions:
        conditions_by_name[c['name']].append(c)
    return conditions_by_name