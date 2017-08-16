import sys

def SieveOfEratosthenes(n):

    res = []
    prime = [True for i in range(n+1)]
    p=2
    while(p * p <= n):

        if (prime[p] == True):
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p+=1
    lis =[]

    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            res.append(p)
    return res

t = int(sys.stdin.readline().strip())
i = []
maxb = 0
for _ in xrange(t):
    l = sys.stdin.readline().strip().split(' ')
    a = int(l[0])
    b = int(l[1])
    k = int(l[2])
    maxb = max(b, maxb)
    i.append((a,b,k))
p = SieveOfEratosthenes(maxb)
ssp = set(p)
# print p[:100]
d = 1
for e in i:
    # import pdb; pdb.set_trace()
    sp = 0
    abc = []
    for j in xrange(e[0], e[1]+1):
        c = 0
        if j not in ssp:
            for k in p:
                if k > j/2 or c > e[2]:
                    break
                else:
                    if j%k ==0:
                        c+=1
        else:
            c = 1

        if c == e[2]:
            abc.append(j)
            sp += 1
    # print abc
    print "Case #%s: %s" % (d, sp)
    d+=1
