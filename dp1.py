import itertools

def subsetsum(a, k):
    d = {}
    for i in xrange(1, len(a)+1):
        for j in itertools.combinations(a, i):
            if sum(j) == k:
                d[i] = j
    print d



subsetsum([3, 34, 4, 12, 5, 2], 9)
