# 끝나지 않는 파티

import sys

n, m = map(int, sys.stdin.readline().split())
party = []
for i in range(n):
    party.append(list(map(int, sys.stdin.readline().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            party[i][j] = min(party[i][j], party[i][k] + party[k][j])

for i in range(m):
    start, end, time = map(int, sys.stdin.readline().split())

    if party[start - 1][end - 1] > time:
        print('Stay here')
    else:
        print('Enjoy other party')