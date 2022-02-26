# 연속합

n = int(input())
array = list(map(int, input().split()))

d = [0] * n
d[0] = array[0]

for i in range(1, n):
    d[i] = array[i] + max(array[i - 1], d[i - 1], 0)

print(max(d))