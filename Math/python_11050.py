# 이항 계수 1

n, k = map(int, input().split())
a = 1
b = 1

for i in range(n, n - k, -1):
    a *= i

for i in range(k, 1, -1):
    b *= i

print(a//b)