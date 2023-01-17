# 1, 2, 3 더하기 4

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

target = max(array)
dp = [1 for i in range(target + 1)]

for i in range(2, target + 1):
    dp[i] += dp[i - 2]

for i in range(3, target + 1):
    dp[i] += dp[i - 3]
    
for i in array:
    print(dp[i])
