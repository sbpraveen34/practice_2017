import sys

t = int(sys.stdin.readline())
for _ in xrange(0, t):
    i = sys.stdin.readline()
    i = i.strip().split(' ')
    n = int(i[0])
    x = int(i[1])
    y = int(i[2])
    for num in xrange(x, n, x):
        if num % y:
            print num,
    print
