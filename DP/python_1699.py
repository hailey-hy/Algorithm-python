# 제곱수의 합

n = int(input())

d = [0] * (n + 1)
compare = [i * i for i in range(1, 317)]

for i in range(1, n + 1):
    array = []
    for j in compare:
        if j > i:
            break
        array.append(d[i - j])
    d[i] = min(array) + 1