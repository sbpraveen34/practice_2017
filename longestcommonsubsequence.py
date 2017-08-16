l = [[]]

a = "ABAZDC"
b = "ABAZDC"
l = [[None]*len(b)]*len(a)


def sequence(a, b , m, n):

    # print "++++++++++"
    if -1< m < len(a) and -1< n < len(b):
        # print m
        # print n
        # print a[m]
        # print b[n]
        # print "==============="
        if l[m][n]:
            return l[m][n]
        result = None
        if a[m] == b[n]:
            result = 1 + sequence(a, b, m-1, n-1)
            # return l[m][n]
            # return l[m][n]
        else:
            result =  max(sequence(a, b, m-1, n), sequence(a, b, m, n-1))
            # return l[m][n]
            # return l[m][n]
        l[m][n] = result
        return result
    return 0

print sequence(a, b, len(a)-1, len(b)-1)
for i in l:
    print i
