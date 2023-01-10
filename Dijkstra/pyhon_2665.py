# 미로만들기

import sys
import heapq

n = int(input())

rooms = []
for _ in range(n):
    tmp = input()
    tmp_array = []
    for room in tmp:
        if room == '0':
            tmp_array.append(1)
        else:
            tmp_array.append(0)
    rooms.append(tmp_array)

memos = [[sys.maxsize] * n for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dijkstra(x, y):
    q = []
    heapq.heappush(q, (0, x, y))
    while q:
        cost, x, y = heapq.heappop(q)
        if memos[x][y] < cost:
            continue
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < n and memos[new_x][new_y] == sys.maxsize:
                new_cost = cost + rooms[new_x][new_y]
                memos[new_x][new_y] = new_cost
                heapq.heappush(q, (new_cost, new_x, new_y))

dijkstra(0, 0)
print(memos[n - 1][n - 1])
