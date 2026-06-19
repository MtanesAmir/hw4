def calculate_betweenness_centrality(graph) -> dict:
    """
    Calculates Betweenness Centrality for all nodes in the graph using Brandes' algorithm.
    """
    nodes = list(graph.nodes.keys())
    cb = {v: 0.0 for v in nodes}
    
    for s in nodes:
        # Stack for accumulation
        stack = []
        # Predecessors list
        predecessors = {v: [] for v in nodes}
        # Path count from s
        sigma = {v: 0 for v in nodes}
        sigma[s] = 1
        # Distance from s
        dist = {v: -1 for v in nodes}
        dist[s] = 0
        
        # BFS queue
        queue = [s]
        
        while queue:
            u = queue.pop(0)
            stack.append(u)
            for v in graph.adjacency.get(u, []):
                # Node v found for first time
                if dist[v] < 0:
                    queue.append(v)
                    dist[v] = dist[u] + 1
                # Shortest path through u
                if dist[v] == dist[u] + 1:
                    sigma[v] += sigma[u]
                    predecessors[v].append(u)
                    
        # Accumulation
        dependency = {v: 0.0 for v in nodes}
        while stack:
            w = stack.pop()
            for v in predecessors[w]:
                dependency[v] += (sigma[v] / sigma[w]) * (1.0 + dependency[w])
            if w != s:
                cb[w] += dependency[w]
                
    # Normalize and adjust for undirected graph
    # For undirected graphs, divide by 2 because each path is counted twice (s->t and t->s)
    # Normalization factor: (N-1)(N-2)/2 if N > 2, else 1
    # So we divide by (N-1)*(N-2)
    N = len(nodes)
    if N > 2:
        divider = (N - 1) * (N - 2)
    else:
        divider = 2.0
        
    for v in cb:
        cb[v] = cb[v] / divider
        
    return cb
