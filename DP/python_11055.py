# 증가하는 부분 수열의 합 찾기

n = int(input())
array = list(map(int, input().split()))
d = [x for x in array]

for i in range(n):
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + array[i])

print(max(d))