# 지름길

import heapq
n, D = map(int, input().split())

now = 0
result = 0

shorts = [[] for _ in range(D + 1)]
for i in range(D):
    shorts[i].append((i + 1, 1))

for i in range(n):
    start, end, distance = map(int, input().split())
    if end > D:
        continue
    shorts[start].append((end, distance))

INF = 987654321
distance = [INF] * (D + 1)
distance[0] = 0

queue = []
heapq.heappush(queue, (0, 0))

while queue:
    d, now = heapq.heappop(queue) #현재 비용, 현재 위치
    if distance[now] < d:
        continue
    for i in shorts[now]:
        cost = d + i[1] #현재 비용 + 목적지 비용
        if distance[i[0]] > cost: #새로 산정된 목적지 비용이 더 쌀 경우
            distance[i[0]] = cost
            heapq.heappush(queue, (cost, i[0])) #새로 산정된 목적지 비용, 목적지 위치 업데이트
        

print(distance[D])