#!/bin/python

import sys
import operator
from collections import defaultdict

def isValid(s):
    # Complete this function
    d = defaultdict(int)
    v = defaultdict(int)
    isp = False
    for i in s:
        d[i] += 1
    
    m = 0
    for j in d.values():
        v[j] += 1
    m = max(v.items(), key=operator.itemgetter(1))[0]
    c = 0
    diff = 0

    for i in d:
        if d[i] != m:
            c += 1
            diff = min(d[i], abs(m-d[i]))

    if c <2 and diff <=1:
        return "YES"
    else:
        return "NO"

s = raw_input().strip()
result = isValid(s)
print(result)
