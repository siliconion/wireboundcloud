from Queue import Queue


def mark_opposite(category):
    if category == -1:
        return -1
    if category == 1:
        return 2
    return 1


def bipartite(adj):
    q = Queue()
    categories = [-1] * len(adj)
    for v in range(len(adj)):
        q.put(v)
    while not q.empty():
        v = q.get()
        if categories[v] > 0:
            for neighbor in adj[v]:
                if categories[neighbor] > 0 and categories[v] == categories[neighbor]:
                    return False
        for neighbor in adj[v]:
            if categories[neighbor] > 0:
                if categories[v] < 0:
                    categories[v] = mark_opposite(categories[neighbor])
                else:
                    if categories[v] == categories[neighbor]:
                        return False
            else:
                categories[neighbor] = mark_opposite(categories[v])

    return True
