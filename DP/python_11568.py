# 민균이의 계략

import sys
input = sys.stdin.readline

n = int(input())

card = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1,n):
    max_value = 0
    for j in range(i):
        if card[j] < card[i]:
            max_value = max(max_value, dp[j]) #검증 대상(card[j])의 증가하는 순열 기록에 +1하기 위해 dp[j]를 사용
            # max_value = max_value + 1
        
    dp[i] = max_value + 1

print(max(dp))