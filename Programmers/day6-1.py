# 더 맵게

from heapq import *

def solution(scoville, K):
    heap = []
    for i in scoville:
        heappush(heap, i)

    answer = 0
    while True:
        if len(heap) < 2 and heap[0] < K:
            return -1
        elif heap[0] < K:
            first = heappop(heap)
            second = heappop(heap)
            heappush(heap, first + second * 2)
            answer += 1
        else:
            return answer

    