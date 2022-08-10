# 숫자 카드

import sys

n = int(sys.stdin.readline())

cards = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

def binary(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in nums:
    if binary(cards, i, 0, n - 1) is not None:
        print(1, end=' ')

    else:
        print(0, end=' ')