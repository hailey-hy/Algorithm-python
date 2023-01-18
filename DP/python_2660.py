# 회장뽑기

import sys
import heapq

n = int(input())
graph = [[] for _ in range(n + 1)]
answer = []
while True:
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        graph[x].append(y)
        graph[y].append(x)
    else:
        break

def floid(x):
    q = []
    tmp = [sys.maxsize] * (n + 1)
    tmp[0] = 0
    tmp[x] = 0
    for j in graph[x]:
        heapq.heappush(q, (1, j))
    while q:
        x = heapq.heappop(q)
        if tmp[x[1]] > x[0]:
            tmp[x[1]] = x[0]
        for k in graph[x[1]]:
            if tmp[k] == sys.maxsize:
                heapq.heappush(q, (x[0] + 1, k))
    return max(tmp)
        
            
for i in range(1, n + 1):
    answer.append(floid(i))
    
candidate = min(answer)
print(candidate, answer.count(candidate))
for i in range(n):
    if answer[i] == candidate:
        print(str(i + 1), end=' ')