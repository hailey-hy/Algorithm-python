# 해킹

import heapq
import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for tmp in range(n + 1)]
    infected = [sys.maxsize] * (n + 1)
    for i in range(d):
        a, b, second = map(int, sys.stdin.readline().split())
        graph[b].append((second, a))
    
    infected[c] = 0
    q = []
    heapq.heappush(q, (0, c))

    while q:
        second, now = heapq.heappop(q)
        for i in graph[now]:
            new_second = i[0] + second
            if new_second < infected[i[1]]:
                infected[i[1]] = new_second
                q.append((new_second, i[1]))
    
    cnt = 0
    maximum = 0
    for i in infected:
        if i < sys.maxsize:
            cnt += 1
            maximum = max(maximum, i)
    print(cnt, maximum)