from collections import defaultdict
import heapq

def max_probability(n, edges, succProb, start, end):
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        prob = succProb[i]
        adj[u].append((v, prob))
        adj[v].append((u, prob))
    max_prob = [0.0] * n
    max_prob[start] = 1.0
    pq = [(-1.0, start)]  

    while pq:
        neg_p, u = heapq.heappop(pq)
        p = -neg_p
        if p < max_prob[u]:
            continue
        if u == end:
            return p
        for v, edge_p in adj[u]:
            new_prob = p * edge_p
            if new_prob > max_prob[v]:
                max_prob[v] = new_prob
                heapq.heappush(pq, (-new_prob, v))

    return max_prob[end]
