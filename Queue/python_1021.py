# 회전하는 큐

from collections import deque
        
n, m = map(int, input().split())

q = deque([i for i in range(1, n + 1)])

nums = list(map(int, input().split()))

total = 0

for i in nums:
    while m > 0:
        if q[0] == i:
            q.popleft()
            break
        else:
            total += 1
            if q.index(i) >= len(q)//2 + 1:
                q.appendleft(q.pop())
            else:
                q.append(q.popleft())
    
    m -= 1

print(total)
