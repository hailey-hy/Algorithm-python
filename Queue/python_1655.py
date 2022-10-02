# 가운데를 말해요

import heapq
import sys

n = int(sys.stdin.readline())
left = []
right = []


for i in range(n): #0, 1, 2
    num = int(sys.stdin.readline())

    if i % 2 == 0:
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)

    if left and right and -left[0] > right[0]:
        tmp_left = heapq.heappop(left)
        tmp_right = heapq.heappop(right)

        heapq.heappush(left, -tmp_right)
        heapq.heappush(right, -tmp_left)

    print(-left[0])