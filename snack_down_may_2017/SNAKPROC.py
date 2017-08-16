import sys

n = int(sys.stdin.readline().strip())

for _ in xrange(0, n):
    k = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    start = 0
    is_valid = True
    for i in s:
        if i == 'H':
            if start:
                is_valid = False
                break;
            start = 1
        elif i == 'T':
            if not start:
                is_valid = False
                break;
            start = 0
    if start:
        print "Invalid"
    else:
        if is_valid:
            print "Valid"
        else:
            print "Invalid"
