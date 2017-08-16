def max_sub_product(a):
    s = [-999999999999]*len(a)
    s[0] = a[0]
    for i in xrange(1,len(a)):
        if a[i-1] < 0 and a[i] < 0:
            # import pdb; pdb.set_trace()
            s[i] = max(a[i]*a[i-1]*s[i-1], s[i-1], a[i]*a[i-1])
        else:
            s[i] = max(a[i]*s[i-1], a[i])

    print s


a = [6, -3, -10, 0, 2]

max_sub_product(a)
