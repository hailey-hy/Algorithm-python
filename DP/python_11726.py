# 2*n 타일링
# 규칙은 피보나치 수열이므로 DP로 해결

n = int(input())
d = [1] * (n + 1)

for i in range(2, n + 1):
    d[i] = d[i - 2] + d[i - 1]

print(d[n] % 10007)
