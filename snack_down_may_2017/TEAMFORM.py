import sys

t = int(sys.stdin.readline().strip())

for _ in xrange(0, t):
    r = sys.stdin.readline().strip().split(' ')
    n = int(r[0])
    m = int(r[1])
    for __ in xrange(0, m):
        q = sys.stdin.readline()

    if (n - 2*m) % 2:
        print 'no'
    else:
        print 'yes'
