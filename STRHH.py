import sys

t = int(sys.stdin.readline())

for _ in xrange(0, t):
    s = sys.stdin.readline().strip()
    lens = len(s)
    if lens == 2:
        print s[0]
        continue
    for i in xrange(0, len(s)/2, 2):
        sys.stdout.write(s[i])
    print
