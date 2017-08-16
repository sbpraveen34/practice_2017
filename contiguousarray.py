s = []
def contiguoussum(a, pos):

    if pos ==0:
        print "{}   {}".format(pos, a[0])
        return a[0]
    # if s[pos]:
    #     return s[pos]
    abc = max(a[pos], contiguoussum(a, pos-1)+a[pos])
    print "{}   {}".format(pos, abc)
    return abc




a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = [None]*len(a)
s[0] = a[0]
print contiguoussum(a, len(a)-1)
# print s
