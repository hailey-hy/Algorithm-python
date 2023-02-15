# 가장 긴 증가하는 부분 수열 4

n = int(input())
array = list(map(int, input().split()))
dp = [1] * (n + 1)
answer = []

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
x = max(dp)

result = []
for i in range(n-1, -1, -1):
    if dp[i] == x:
        result.append(array[i])
        x -= 1
result.reverse()
for r in result:
    print(r, end=' ')
