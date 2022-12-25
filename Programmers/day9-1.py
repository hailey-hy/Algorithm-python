# 피로도

from collections import deque
from itertools import permutations

def solution(k, dungeons):
    answer = -1
    length = len(dungeons)
    max_result = 0
    for i in permutations(dungeons, length):
        tmp = k
        result = 0
        for j in i:
            if j[0] <= tmp:
                tmp -= j[1]
                result += 1
            else:
                break
        max_result = max(result, max_result)
            
    return max_result