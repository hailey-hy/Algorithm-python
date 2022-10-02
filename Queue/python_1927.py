# 최소 힙

import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num > 0:
        heapq.heappush(heap, num)
    else:
        if len(heap) > 0:
            print(heapq.heappop(heap))
        else:
            print(0)