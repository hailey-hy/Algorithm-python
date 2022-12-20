# 단지번호붙이기

from collections import deque

n = int(input())

houses = [list(input()) for _ in range(n)]
cnt = 0
cnt_list = []

def bfs(x, y):
    queue = deque([(x, y)])
    tmp = 0
    while queue:
        now_x, now_y = queue.popleft()
        if now_x >= n or now_y >= n or now_x < 0 or now_y < 0:
            continue
        else:
            if houses[now_x][now_y] == '1':
                tmp += 1
                houses[now_x][now_y] = '0'
                queue.append((now_x + 1, now_y))
                queue.append((now_x, now_y + 1))
                queue.append((now_x - 1, now_y))
                queue.append((now_x, now_y - 1))
    return tmp

for i in range(n):
    for j in range(n):
        if houses[i][j] != '0':
            cnt += 1
            cnt_list.append(bfs(i, j))

print(cnt)
cnt_list.sort()
for i in cnt_list:
    print(i)
