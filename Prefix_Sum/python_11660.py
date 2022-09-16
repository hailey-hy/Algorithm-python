# 구간 합 구하기 5

import sys

n, m = map(int, sys.stdin.readline().split())
table = []
table_sum = []
table_sum.append([0] * (n + 1))

for i in range(n):
    table.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    table_sum.append([0])
    for j in range(n):
        table_sum[i + 1].append(table_sum[i + 1][j]+ table[i][j] + table_sum[i][j + 1] - table_sum[i][j])


for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    print(table_sum[x2][y2] - table_sum[x2][y1 - 1] - table_sum[x1 - 1][y2] + table_sum[x1 - 1][y1 - 1])