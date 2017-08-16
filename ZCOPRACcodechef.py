import sys

def func():
    line = sys.stdin.readline()
    line.strip()
    n = int(line.split()[0].strip())
    h = int(line.split()[1].strip())

    line = sys.stdin.readline()
    line = line.strip()
    a = map(lambda x: int(x.strip()), line.split())

    line = sys.stdin.readline()
    line = line.strip()
    step = map(lambda x: int(x.strip()), line.split())

    step = step[:len(step)-1]
    import pdb; pdb.set_trace()
    pos = 0
    l = 0

    for i in xrange(0, len(step)):
        if(i == 1):
            if pos > 0:
                pos -= 1
        if(i == 2):
            if pos < n-1:
                pos += 1
        if(i == 3):
            if a[pos]:
                a[pos] -= 1
        if(i == 4):
            if a[pos] < h:
                a[pos] += 1

    print ' '.join(a)
