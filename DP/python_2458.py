# 키 순서

import sys

n, m = map(int, input().split())
students = [[0] * n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    students[a - 1][b - 1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            if students[i][k] == 1 and students[k][j] == 1:
                students[i][j] = 1

answer = 0
for i in range(n):
    check = 0
    for j in range(n):
        check += students[i][j] + students[j][i]
    if check == n - 1:
        answer += 1
print(answer)