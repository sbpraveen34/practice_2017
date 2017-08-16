import sys

for _ in xrange(0, 10):
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    a = (n-k) >> 1
    print a + k
    print a
