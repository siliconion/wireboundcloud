class Graph():
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.entered = [False] * self.size
        self.left = [False] * self.size

    def explore(self, index):
        if self.entered[index] and not self.left[index]:
            return False
        if self.left[index] is True:
            return True
        self.entered[index] = True
        for neighbor in self.adj[index]:
            if not self.explore(neighbor):
                return False
        self.left[index] = True
        return True

    def acyclic(self):
        for index in range(self.size):
            if self.explore(index):
                return 1
        return 0


def acyclic(adj):
    graph = Graph(adj)
    return graph.acyclic()
