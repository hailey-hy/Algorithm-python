# 정수 a를 k로 만들기

from collections import deque
import sys

a, k = map(int, sys.stdin.readline().split())
record = [1000001 for _ in range(1000001)]
record[a] = 0

def bfs(a):
    queue = deque([a])
    while queue:
        number = queue.popleft()
        if number == k:
            break
        if number + 1 < k:
            if record[number + 1] > record[number] + 1:
                record[number + 1] = record[number] + 1
                queue.append(number + 1)
        if number * 2 < k:
            if record[number * 2] > record[number] + 1:
                record[number * 2] = record[number] + 1
                queue.append(number * 2)
        
bfs(a)
print(record[k - 1])
