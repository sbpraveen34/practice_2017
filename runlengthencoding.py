import sys
from collections import defaultdict

a = sys.stdin.readline().strip()
b = []
count = 1
for i in xrange(0, len(a)-1):
    if a[i] == a[i+1]:
        count += 1
    else:
        b.append(a[i])
        b.append(str(count))
        count = 1

b.append(a[-1])
b.append(str(count))
print ''.join(b)
