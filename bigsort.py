#!/bin/python

import sys
def cmpa(a, b):
    # import pdb; pdb.set_trace()
    if len(a) < len(b):
        return False
    elif len(a) == len(b):
        for i in xrange(len(a)):
            if int(a[i]) < int(b[i]):
                return False
            elif int(a[i]) > int(b[i]):
                return True
    else:
        return True

n = int(raw_input().strip())
unsorted = []
unsorted_i = 0
for unsorted_i in xrange(n):
    unsorted_t = str(raw_input().strip())
    unsorted.append(unsorted_t)
a = sorted(unsorted, cmp=cmpa)
print a
for i in unsorted:
    print str(i)
# your code goes here
