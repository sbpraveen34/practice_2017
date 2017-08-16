def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """

    binx = bin(x).split('b')[1]
    biny = bin(y).split('b')[1]
    c = 0
    if len(binx) > len(biny):
        biny = biny.zfill(len(binx))
    else:
        binx = binx.zfill(len(biny))

    for i in xrange(0, len(binx)):
        if binx[i] != biny[i]:
            c += 1

    return c
