# 미팅

from itertools import product

n, m, c = map(int, input().split())

happy = []
for _ in range(c):
    happy.append(list(map(int, input().split())))

info = []
for _ in range(2):
    info.append(list(map(int, input().split())))

info_a = []
for i in range(n):
    info_a.append(i)

info_b = []
for i in range(m):
    info_b.append(i)

combination = list(product(info_a, info_b))
total = 0

for i in range(len(combination)):
    tmp_a = [combination[i][0]]
    tmp_b = [combination[i][1]]
    tmp_total = happy[info[0][combination[i][0]] - 1][info[1][combination[i][1]] - 1]
    for j in range(i + 1, len(combination)):
        if combination[j][0] in tmp_a or combination[j][1] in tmp_b:
            continue
        else:
            tmp_a.append(combination[j][0])
            tmp_b.append(combination[j][1])
            tmp_total += happy[info_a[combination[j][0]]][info_b[combination[j][1]]]
    total = max(total, tmp_total)

print(total)