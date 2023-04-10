# 카드 정렬하기

import heapq

n = int(input())
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

total = 0

while len(heap) >= 2:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    tmp = first + second
    total += tmp
    heapq.heappush(heap, tmp)

print(total)