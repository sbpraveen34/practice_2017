import sys

l = sys.stdin.readline()
l = map( lambda x: int(x), l.strip().split(' '))
x = l[0]
y = l[1]

if x == y:
    print 0
else:
    print 1
