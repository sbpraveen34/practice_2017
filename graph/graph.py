class Node:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self, n):
        self.edge = [ [] for _ in xrange(0, n) ]
        self.nodes = []
    def addEdge(self, i, j):
        self.edge[i].append(j)
        # self.edge[j].append(i)

    def bfs(self):
        start = 2
        visited = [ 0 for _ in xrange(len(self.edge))]
        stack = []
        stack.append(start)
        while (stack):
            current = stack.pop()
            if not visited[current]:
                print current
                visited[current] = 1
                for node in self.edge[current]:
                    stack.append(node)
    def dfs(self, start)
        


g = Graph(5)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.bfs()
