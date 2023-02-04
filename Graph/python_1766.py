# 문제집

import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topology():
    result = []
    q = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)
    
    for i in result:
        print(i, end = ' ')

topology()