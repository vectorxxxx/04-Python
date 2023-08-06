# -*- coding: utf-8 -*-
from functools import reduce
import logging
import pdb

def str2num(s):
    try:
        return int(s)
    except Exception as e:
        pdb.set_trace()
        print(s, type(s))
        logging.exception(e)
        return float(s)
        

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
