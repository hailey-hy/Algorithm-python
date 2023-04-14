# 보석 도둑

import heapq
import sys

n, k = map(int, sys.stdin.readline().split())

heap = []
for _ in range(n):
    m, v = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (m, v))

bags = []
for _ in range(k):
    bags.append(int(sys.stdin.readline()))
bags.sort()

answer = 0
jewl = []
for bag in bags:
    while heap and bag >= heap[0][0]:
        heapq.heappush(jewl, -heapq.heappop(heap)[1])
    if jewl:
        answer -= heapq.heappop(jewl)
    elif not heap:
        break

print(answer)