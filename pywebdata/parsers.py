import re
import operator

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
        
    return map(make_cond_dict, qry.split('and'))
    
if __name__ == '__main__':

    for i in parse_query('damon = 5 and m1ke >= 6.0 and b = 203948.09238'):
        print i
