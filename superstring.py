#!/bin/python

import sys
from collections import defaultdict

s_len = int(raw_input().strip())
s = raw_input().strip()
d = set()
for i in s:
    d.add(i)
d = list(d)
m = 0
isp = True
for k in xrange(len(d)):
    for l in xrange(k+1, len(d)):
        if k != l:
            r = []
            f = 0
            g = set()
            isp = True
            for i in s:
                if i == d[k] or i == d[l]:
                    r.append(i)
            for j in xrange(len(r)-1):
                if r[j] != r[j+1] and len(g) <= 2:
                    g.add(r[j])
                else:
                    isp = False
                    break
            if isp:
                m = max(m, len(r))


print m
