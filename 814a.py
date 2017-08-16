import sys


def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]

l = sys.stdin.readline().strip().split(' ')
n = int(l[0])
k = int(l[1])

a = map(int, sys.stdin.readline().strip().split(' '))
b = map(int, sys.stdin.readline().strip().split(' '))
r = False
for i in xrange(len(a)):
    if i == 0:
        continue
    elif i == n -1 :
        continue
    else:
        if a[i] == 0:
            # import pdb; pdb.set_trace()
            for j in b:
                if a[i-1] > j < a[i+1] or a[i-1] > j > a[i+1] or a[i-1] < j > a[i+1]:
                    r = True
                    break

if r:
    print "YES"
else:
    print "NO"
