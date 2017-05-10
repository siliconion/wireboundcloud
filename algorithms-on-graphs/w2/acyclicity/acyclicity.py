class Graph():
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.visited = [False] * self.size

    def explore(self, index, visited):
        if visited[index] is True:
            return True
        visited[index] = True
        for neighbor in self.adj[index]:
            if self.explore(neighbor, list(visited)):
                return True
        return False

    def acyclic(self):
        for index in range(self.size):
            if self.explore(index, [False] * self.size):
                return 1
        return 0


def acyclic(adj):
    graph = Graph(adj)
    return graph.acyclic()
