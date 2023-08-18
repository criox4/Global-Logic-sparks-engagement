from collections import defaultdict, deque

def shortest_path_faster_algorithm(V, S, arr):
    graph = defaultdict(list)
    for u, v, w in arr:
        graph[u].append((v, w))
    
    d = [float('inf')] * (V + 1)
    d[S] = 0
    
    queue = deque([S])
    in_queue = [False] * (V + 1)
    in_queue[S] = True
    
    while queue:
        u = queue.popleft()
        in_queue[u] = False
        
        for v, w in graph[u]:
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True
    
    return d[1:]

