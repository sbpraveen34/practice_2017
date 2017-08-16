import math

def recurse(a, n):
    l = int(math.floor(pow(a, float(1)/n)))
    c = 0
    for i in xrange(l, 0, -1):
        if recursion(a, 0, i, n):
            c+=1
    print c

def recursion(a, k, i, n):
    import pdb; pdb.set_trace()
    if i > 1:
        if k + pow(i, n) == a:

            return True
        elif k + pow(i, n) > a:
            return False
        elif k + pow(i, n) < a:
            return recursion(a, k+pow(i, n), i-1, n)
    elif i == 1:
        return k + 1 == a
    else:
        return False


recurse(10, 2)
