# 회전 초밥

from collections import defaultdict
import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = [int(sys.stdin.readline()) for _ in range(n)]
result = 0

left, right = 0, k - 1
dic = defaultdict(int)
for i in range(k):
    dic[sushi[i]] += 1

dic[c] += 1

while left < n:
    result = max(len(dic), result)
    
    dic[sushi[left]] -= 1
    if dic[sushi[left]] == 0:
        del dic[sushi[left]]
    
    left += 1
    right += 1
    dic[sushi[right % n]] += 1

print(result)