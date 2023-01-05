# DSLR

from collections import deque
import sys

t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    visited = [False] * 100001
    queue = deque([(a, '')])
    visited[a] = True
    while queue:
        now, order = queue.popleft()
        if now == b:
            print(order)
            break
        # D연산
        tmp = (now * 2) % 10000
        if not visited[tmp]:
            queue.append((tmp, order + 'D'))
            visited[tmp] = True
        # S연산
        tmp = (now - 1) % 10000
        if not visited[tmp]:
            queue.append((tmp, order + 'S'))
            visited[tmp] = True
        # L연산
        tmp = (10*now+(now//1000))%10000
        if not visited[tmp]:
                queue.append((tmp, order + 'L'))
                visited[tmp] = True
        # R연산
        tmp = (now//10+(now%10)*1000)%10000
        if not visited[tmp]:
                queue.append((tmp, order + 'R'))
                visited[tmp] = True