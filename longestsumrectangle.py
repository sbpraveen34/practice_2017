def getsum(l, x1, x2, y1, y2):
    s = 0
    for i in xrange(x1, x2+1):
        for j in xrange(y1, y2+1):
            s += l[i][j]
    return s

staticv = 1
d = {}
def sumrectangle(l, x1, x2, y1, y2):
    if x1 == y1 == x2 == y2 == 0:
        print "at zero"
        print "======================"
        return l[0][0]
    if -1 < x1 < len(l) and -1 < x2 < len(l) and -1 < y1 < len(l[0]) and -1 < y2 < len(l[0]):
        if (x1, x2, y1, y2) in d:
            return d[(x1, x2, y1, y2)]

        b =  max(
            sumrectangle(l, x1+1, x2, y1, y2),
            sumrectangle(l, x1, x2-1, y1, y2),
            sumrectangle(l, x1, x2, y1+1, y2),
            sumrectangle(l, x1, x2, y1, y2-1),
            getsum(l, x1, x2, y1, y2)
        )

        d[(x1, x2,y1, y2)] = b
        return b

    else:
        return 0


l = [
        [8, -1],
        [-1, 4]
    ]
d = {}
print sumrectangle(l, 0, len(l)-1, 0, len(l[0])-1)
print len(d)
