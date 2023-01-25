# 운동

import sys

v, e = map(int, sys.stdin.readline().split())

towns = [[sys.maxsize] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    towns[a][b] = c

for k in range(v + 1):
    for i in range(v + 1):
        for j in range(v + 1):
            towns[i][j] = min(towns[i][j], towns[i][k] + towns[k][j])

answer = sys.maxsize
for i in range(1, v + 1):
    for j in range(1, v + 1):
        if towns[i][j] < sys.maxsize and towns[j][i] < sys.maxsize:
            answer = min(answer, towns[i][j] + towns[j][i])
print(answer if answer < sys.maxsize else -1)