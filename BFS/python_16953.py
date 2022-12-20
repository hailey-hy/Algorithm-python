#  A -> B

from collections import deque
a, b = map(int, input().split())

queue = deque([(a, 1)])
while queue:
    x, t = queue.popleft()
    if x == b:
        print(t)
        break
    if x > b:
        continue
    queue.append((x * 2, t + 1))
    queue.append((int(str(x) + '1'), t + 1))
else:
    print(-1)