import sys
from collections import defaultdict

def dfs(edges, visited, start, parent):
    # import pdb; pdb.set_trace()
    visited[start] = True
    for i in edges[start]:
        if not visited[i]:
            if dfs(edges, visited, i, start):
                return True
        elif i != parent:
            return True
    return False


def dfss(edges, n):
    visited = [False]*(n+1)

    for i in xrange(1,n+1):
        if not visited[i]:
            if dfs(edges, visited, i, -1):
                return True

    return False


n, m = map(int, sys.stdin.readline().strip().split(' '))
nodes = range(1, n+1)
edges = defaultdict(list)

for i in xrange(m):
    j, k = map(int, sys.stdin.readline().strip().split(' '))
    edges[j].append(k)
    edges[k].append(j)

if dfss(edges, n):
    print "NO"
else:
    print "YES"
