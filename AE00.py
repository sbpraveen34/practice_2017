import sys
import math

n = int(sys.stdin.readline())
s = 1
if n < 4:
    print n
else:
    s = 3
    for i in xrange(4, n+1):
        f = 0
        for k in xrange(1, int(math.sqrt(i))+1):
            if i % k == 0:
                f += 1
        s += f
    print s
