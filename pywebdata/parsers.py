import re
import operator

#borrowed from standard library distutils.versionpredicate

compmap = {
    "<": operator.lt, 
    "<=": operator.le, 
    "==": operator.eq,
    ">": operator.gt, 
    ">=": operator.ge, 
    "!=": operator.ne
}

condition_splitter = re.compile(r'\s*(\D\w*)\s*(<=|>=|<|>|!=|=)\s*(\d*\.*\d*)')

def parse_query(qry_str):
    conditions = qry_str.split('and')
    return map(lambda x:condition_splitter.match(x).groups(), conditions)
    
if __name__ == '__main__':

    a = parse_query('damon = 5 and m1ke >= 6.0 and b = 203948.09238')
    print a