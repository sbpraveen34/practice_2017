import sys

t = int(sys.stdin.readline().strip())

while t:
    t -= 1
    n = int(sys.stdin.readline().strip())
    a = sys.stdin.readline().strip().split()
    result = True
    h = {
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
    }
    if n % 2:
        if a[n/2] == '7':
            for i in xrange(0, n/2):
                if a[i] != a[n-i-1]:
                    result = False
                    break
        else:
            result = False
    else:
        result = False

    if result:
        print "yes"
    else:
        print "no"
