class Graph():
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.visited = [False] * self.size
        self.toposort_stack = []

    def dfs(self, index):
        if not self.visited[index]:
            self.visited[index] = True
            for neighbor in self.adj[index]:
                self.dfs(neighbor)
            self.toposort_stack.append(index)

    def toposort(self):
        self.toposort_stack = []
        for index in range(self.size):
            self.dfs(index)
        print self.toposort_stack

        return self.toposort_stack[::-1]


def toposort(adj):
    graph = Graph(adj)
    return graph.toposort()
