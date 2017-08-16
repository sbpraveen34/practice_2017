#!/bin/python

import sys

def grid_search(G, P, m, n):
    import pdb; pdb.set_trace()
    for i in xrange(len(P)):
        for j in xrange(len(P[i])):
            if not(m+i < len(G) and n+j < len(G[m+i]) and P[i][j] == G[m+i][n+j]):
                return False
    return True



t = int(raw_input().strip())

for a0 in xrange(t):
    R,C = raw_input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in xrange(R):
        G_t = str(raw_input().strip())
        G.append(G_t)
    r,c = raw_input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in xrange(r):
        P_t = str(raw_input().strip())
        P.append(P_t)
    result = "NO"
    try:
        import pdb; pdb.set_trace()
        for i in xrange(len(G)):
            for j in xrange(len(G[i])):
                if G[i][j] == P[0][0] and grid_search(G, P, i, j):
                    result="YES"
                    raise Exception("kdkdkdkd")
    except Exception, e:
        pass
    print result
