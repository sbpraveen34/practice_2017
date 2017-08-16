def increasingsubsequence(a, pos):
    if pos == 0:
        return 1, a[pos]

    length, maxn = increasingsubsequence(a, pos-1)

    if a[pos] > maxn:
        maxn = a[pos]
        length += 1
        print length, maxn

    return length, maxn


a = [3, 10, 2, 1, 20]
s = [(None, None)]*len(a)
s[0] = (1, a[0])
for i in xrange(len(a)):
    print "{}      {}".format(i, a[i])
print increasingsubsequence(a, len(a)-1)
