import sys


n = int(sys.stdin.readline().strip())
l = []
for _ in xrange(n):
    l.append(sys.stdin.readline().strip())

d = {}
tofind = l[-1].split(' = ')[0]
for exp in l:
    expi = exp.split(' = ')
    intfound = False
    try:
        d[expi[0]] = int(expi[1])
        intfound = True
    except:
        pass
    if not intfound:
        d[expi[0]] = expi[1]
