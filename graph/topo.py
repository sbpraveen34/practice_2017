class Node:
    def __init__(self, val):
        self.val = val

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in xrange(n)]
        self.visited = [0]*n
        self.stack = []
    def add_edge(self, n1, n2):
        self.adj[n1].append(n2)
    def topoutil(self, i):
        self.visited[i] = True
        for j in self.adj[i]:
            if not self.visited[j]:
                self.topoutil(j)
        self.stack.append(i)

    def toposort(self):
        for i in xrange(self.n):
            if not self.visited[i]:
                self.topoutil(i)
        
a = ["baa", "abcd", "abca", "cab", "cad"]
g = Graph(4)
for i in xrange(len(a)-1):
    w1 = a[i]
    w2 = a[i+1]
    for j in xrange(min(len(w1), len(w2))):
        if w1[j] != w2[j]:
            print w1
            print w2
            print w1[j]
            print w2[j]
            g.add_edge(ord(w1[j]) - ord('a'), ord(w2[j]) - ord('a'))
            break

g.toposort()
