# 맥주 마시면서 걸어가기

from collections import deque
import math

t = int(input())
for _ in range(t):
    store_num = int(input())
    node = []
    start_x, start_y = map(int, input().split())
    for i in range(store_num):
        node.append(list(map(int, input().split())))
    fest_x, fest_y = map(int, input().split())
    node.append([fest_x, fest_y])

    visited = [False] * (store_num + 1)

    def bfs(a, b):
        q = deque([(a, b)])
        while q:
            x, y = q.popleft()
            if x == fest_x and y == fest_y:
                return 'happy'
            # if 0 < beer:
            for index, i in enumerate(node):
                if not visited[index]:
                    distance = abs(x - i[0]) + abs(y - i[1])
                    if 20 >= math.ceil(distance / 50):
                        visited[index] = True
                        q.append((i[0], i[1]))
        return 'sad'

    print(bfs(start_x, start_y))