def commonsubsequence(a, b):
    s = set()
    for i in xrange(1, pow(2,len(a))):
        c = []
        for j in xrange(len(a)):
            if i & (1<<j):
                c.append(a[j])
        s.add(tuple(c))
    for i in s:
        print i


commonsubsequence("abcdefgh", "jdjdj")
