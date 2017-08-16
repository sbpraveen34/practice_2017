from collections import defaultdict

def getset(a, k):
    d = defaultdict(list)
    dl = defaultdict(int)
    l = []

    for i in a:
        d[i%k].append(i)
        dl[i%k]+=1
    print d
    print dl
    for e in xrange(1, k//2+1):
        print e
        print dl[e]
        print d[e]
        print dl[k-e]
        print d[k-e]
        print
        print
        if dl[e] >= dl[k-e]:
            l.extend(d[e])
        else:
            l.extend(d[k-e])
    if dl[0]:
        l.append(d[0][0])
    if k%2 == 0 and dl[k/2]:
        l.append(d[k/2][0])

    print l

getset([1,2,3,4,5,6,7,8,9,10], 4)
