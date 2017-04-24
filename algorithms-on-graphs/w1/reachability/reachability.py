# Given a graph, find is x and y is reachable.
from Queue import Queue


def reach(adj, x, y):
    queue = Queue()
    visited = [False] * len(adj)
    queue.put(x)
    while not queue.empty():
        v = queue.get()
        if v == y:
            return True
        for e in adj[x]:
            if not visited[e]:
                queue.put(e)
                visited[e] = True
    return False

