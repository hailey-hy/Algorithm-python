# 전깃줄

n = int(input())

array = [list(map(int, input().split())) for i in range(n)]

array.sort(key=lambda x:x[0])

wire = [array[i][1] for i in range(n)]

d = [1] * 101

for i in range(n):
    for j in range(i):
        if wire[i] > wire[j]:
            d[i] = max(d[i], d[j] + 1)

print(n - max(d))