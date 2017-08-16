def maxsum(a):
    s = a[0]
    maxh = s
    st = 0
    sp = 0
    for i in xrange(1, len(a)):
        if a[i] > maxh + a[i]:
            st = i
            sp = i
            maxh = a[i]
        else:
            sp = i
            maxh += a[i]

        s = max(s, maxh)

    print s, st, sp


b = [-2, 3, 4, -1, -2, 1, -5, -3]
maxsum(b)
