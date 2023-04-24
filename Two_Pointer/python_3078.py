# 좋은 친구

from collections import defaultdict
import sys

n, k = map(int, sys.stdin.readline().split())
names = [len(sys.stdin.readline().rstrip()) for _ in range(n)]
dic = defaultdict(int)
answer = 0

for i in range(n):
    if i > k:
        dic[names[i - k - 1]] -= 1
    
    answer += dic[names[i]]
    dic[names[i]] += 1

print(answer)
