# 계단 오르기

n = int(input())

stairs = []
for i in range(n):
    stairs.append(int(input()))

d = [0] * 301

d[0] = stairs[0]

if n <= 1:
    pass
elif n <= 2:
    d[1] = stairs[0] + stairs[1]
else:
    d[1] = stairs[0] + stairs[1]
    d[2] = max(stairs[2] + stairs[1], stairs[0] + stairs[2])

for i in range(3, n):
    d[i] = max(d[i - 3] + stairs[i - 1] + stairs[i], d[i - 2] + stairs[i])

print(d[n - 1])