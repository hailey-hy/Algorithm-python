# 최대 힙

import heapq

n = int(input())
heap = []

for i in range(n):
    num = int(input())
    if num > 0:
        heapq.heappush(heap, (-num, num))
    else:
        if len(heap) > 0:
            print(heap[0][1])
            heapq.heappop(heap)
        else:
            print(0)

