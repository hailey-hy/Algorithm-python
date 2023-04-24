# 강의실 배정

import heapq
import sys

n = int(sys.stdin.readline())
classes = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
classes.sort()

q = []
heapq.heappush(q, classes[0][1])

for i in range(1, n):
    if classes[i][0] < q[0]:
        heapq.heappush(q, classes[i][1])
    else:
        heapq.heappop(q)
        heapq.heappush(q, classes[i][1])


print(len(q))