def sort_nearly(a):
    for i in xrange(1, len(a)):
        if a[i] < a[i-1]:
            pos1 = i
    pos2 = 0
    for i in xrange(0, pos1):
        if a[i] > a[pos1-1]:
            pos2 = i

    a[pos1], a[pos2] = a[pos2], a[pos1]
    print a


a = s
sort_nearly(a)
