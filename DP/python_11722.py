# 가장 긴 감소하는 수열

n = int(input())
array = list(map(int, input().split()))
d = [1] * 1001

for i in range(n):
    for j in range(i):
        if array[i] < array[j]:
            d[i] = max(d[i], d[j] + 1)

print(max(d))