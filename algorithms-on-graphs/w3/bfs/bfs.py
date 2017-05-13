from Queue import Queue


def distance(adj, s, t):
    q = Queue()
    dist = [-1] * len(adj)
    dist[s] = 0
    q.put(s)
    while not q.empty():
        current_v = q.get()
        print current_v
        if current_v == t:
            return dist[current_v]
        for neighbor in adj[current_v]:
            if dist[neighbor] < 0:
                dist[neighbor] = dist[current_v] + 1
                q.put(neighbor)
    return -1
