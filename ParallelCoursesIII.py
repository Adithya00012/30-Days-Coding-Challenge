from collections import deque

def minimum_time(n, relations, time):
    adj = [[] for _ in range(n)]
    indegree = [0] * n
    for prevc, nextc in relations:
        p, q = prevc - 1, nextc - 1
        adj[p].append(q)
        indegree[q] += 1
    dp = [0] * n
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            dp[i] = time[i]
            queue.append(i)
    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            dp[nxt] = max(dp[nxt], dp[cur] + time[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return max(dp)

