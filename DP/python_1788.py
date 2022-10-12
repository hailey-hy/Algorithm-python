# 피보나치 수의 확장
# 너무 큰 수를 다루면 메모리 초과가 날 수도 있다!

import sys

n = int(sys.stdin.readline())

dp = [0 for _ in range(1500000)]
dp[1] = 1

if n == 0:
    print(0)
    print(0)

elif n > 0:
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000000
    if dp[n] > 0:
        print(1)
    else:
        print(-1)
    print(dp[n])

else:
    num = abs(n)
    for i in range(2, num + 1):
        data = dp[i - 2] - dp[i - 1]
        if data < 0:
            dp[i] = (abs(data) % 1000000000) * -1
        else:
            dp[i] = data % 1000000000
    if dp[num] > 0:
        print(1)
    else:
        print(-1)
    print(abs(dp[num]))