def res(n):
    if n < 27:
        print chr(n-1 + ord('A'))
    while(n>26):

        print chr(n%26 -1 + ord('A'))
        n = n/26
    print chr(n-1 + ord('A'))
res(705)

def abc(a):
    b = list(a)
    n = 0
    for i in xrange(len(a)):
        # print a[i]
        # print (ord(a[i]) - ord('A') +1)
        # print pow(26, i)
        n += (pow(26, len(a) - i-1)*(ord(a[i]) - ord('A') +1))
        print n

    print n

abc ('V')
