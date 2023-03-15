# 양팔저울

num_c = int(input())
c = list(map(int, input().split()))
num_b = int(input())
b = list(map(int, input().split()))

dp = [False] * 40001
dp[0] = True

for i in range(num_c):
    tmp = set()
    ball = c[i]
    for j in range(40001):
        if dp[j] == True:
            if j + ball <= 40001:
                tmp.add(j + ball)
            if j - ball >= 0:
                tmp.add(j - ball)
            if ball - j >= 0:
                tmp.add(ball - j)
    for k in tmp:
        dp[k] = True

for i in b:
    if dp[i]:
        print('Y', end=' ')
    else:
        print('N', end=' ')