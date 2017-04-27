import sys


class Maze():
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
    maze = Maze(adj)
    return maze.number_of_components()


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
