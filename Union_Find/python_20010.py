# 악덕 영주 혜유

import heapq
import sys

n, k = map(int, sys.stdin.readline().split())

graph = []

for i in range(k):
    a, b, cost = map(int, sys.stdin.readline().split())
    graph.append((cost, a, b))

graph_min = sorted(graph)
parent = [i for i in range(n)]
def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return find(a) == find(b)

def dijkstra(x):
    heap = []
    heapq.heappush(heap, [0, x])
    visited = [-1] * n
    visited[x] = 0
    while heap:
        cost, now = heapq.heappop(heap)
        for n_cost, new in nodes[now]:
            if visited[new] == -1:
                visited[new] = (n_cost + -cost)
                heapq.heappush(heap, [(-n_cost + cost), new])
    return max(visited)

total = 0
nodes = [[] for _ in range(n)]
for cost, a, b in graph_min:
    if not same_parent(a, b):
        union(a, b)
        nodes[a].append((cost, b))
        nodes[b].append((cost, a))
        total += cost
print(total)

maximum = 0
for i in range(n):
    maximum = max(dijkstra(i), maximum)

print(maximum)
