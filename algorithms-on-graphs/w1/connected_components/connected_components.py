class Graph():
    def __init__(self, adj):
        self.adj = adj
        self.size = len(adj)
        self.visited = [False] * self.size

    def explore(self, v_index):
        if not self.visited[v_index]:
            self.visited[v_index] = True
            for neighbor in self.adj[v_index]:
                self.explore(neighbor)
            return 1
        return 0

    def number_of_components(self):
        x = reduce(lambda accu, index: accu + self.explore(index), range(self.size), 0)
        return x


def number_of_components(adj):
    graph = Graph(adj)
    return graph.number_of_components()

