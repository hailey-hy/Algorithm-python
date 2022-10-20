# 1로 만들기 2

n = int(input())

dp = [1000001] * (1000001)
record = [i for i in range(1000001)]

dp[1] = 0
dp[2] = 1
dp[3] = 1

record[1] = 0
record[2] = 1
record[3] = 1

for i in range(4, n + 1):
    tmp1 = n
    tmp2 = n
    if i % 3 == 0:
        tmp1 = dp[i // 3]
    if i % 2 == 0:
        tmp2 = dp[i // 2]
    tmp = min(dp[i - 1], tmp1, tmp2)
    dp[i] = tmp + 1
    if tmp == tmp1:
        record[i] = i // 3
    elif tmp == tmp2:
        record[i] = i // 2
    else:
        record[i] = i - 1

print(dp[n])

if n == 1:
    print(n)
else:
    print(n, end=' ')
    while n > 1:
        print(record[n], end= ' ')
        n = record[n]
