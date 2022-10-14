# 격자상의 경로

n, m, o = map(int, input().split())

def find(n, m):

    dp = [[1] * (m + 1) for _ in range(n + 1)]

    for i in range(n):
        for j in range(m):
            if i > 0 and j > 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n - 1][m -1]

if o == 0:
    print(find(n, m))

else:
    dotN1 = (o-1)//m + 1
    dotM1 = o - (dotN1-1)*m
    dotN2 = n - (dotN1-1)
    dotM2 = m - (dotM1-1)

    first = find(dotN1,dotM1)
    second = find(dotN2,dotM2)

    print(first*second)