import sys

t = sys.stdin.readline()
t = int(t.strip())

for _ in xrange(0, t):
    l = sys.stdin.readline()
    l = l.strip().split(' ')
    n = int(l[0])
    k = int(l[1])
    r = sys.stdin.readline()
    r = map( lambda x: int(x), r.strip().split(' '))
    m = 0
    a = [[0]*n] * n
    for i in xrange(0, n):
        for j in xrange(i+1, n):
            s = sum(r[i:j+1])
            if s == j-i+1:
                if s > m:
                    m = s
            else:
                d = j-i-s+1
                if d <= k:
                    if j-i+1 > m:
                        m = j-i+1

    print m
