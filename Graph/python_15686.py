# 치킨 배달

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
city = []
chicken = 0
chicken_arr = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
min_result = 10e9

for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    city.append(tmp)
    for j in range(n):
        if tmp[j] == 2:
            chicken += 1
            chicken_arr.append((i, j))

def close(chicken, k):
    if chicken == m:
        bfs()
        return
    else:
        for i in range(n):
            for j in range(n):
                if city[i][j] == 2:
                    city[i][j] = 0
                    close(chicken - 1, k + 1)
                    city[i][j] = 2
        # a, b = chicken_arr[i][0], chicken_arr[i][1]
        # city[a][b] = 0
        # close(chicken - 1, i + 1)
        # city[a][b] = 2

def bfs():
    global min_result
    result = 0
    record = [[10e9] * n for _ in range(n)]
    arr2 = []
    arr1 = []
    for i in range(n):
        for j in range(n):
            if city[i][j] == 2:
                arr2.append((i, j))
            elif city[i][j] == 1:
                arr1.append((i, j))

    start = deque(arr2)
    while start:
        x2, y2 = start.popleft()
        end = deque(arr1)
        while end:
            x1, y1 = end.popleft()
            distance = abs(x1 - x2) + abs(y1 - y2)
            if record[x1][y1] > distance:
                record[x1][y1] = distance
    
    for i in range(n):
        for j in range(n):
            if record[i][j] != 10e9:
                result += record[i][j]

    min_result = min(min_result, result)
                            
close(chicken, 0)
print(min_result)