# 가장 긴 증가하는 수열
n = int(input())
d = [1] * 1001 
array = list(map(int, input().split()))

for i in range(n): #기준 인덱스에서 최대 d 값 찾기
    for j in range(i):
        if array[i] > array[j]:
            d[i] = max(d[i], d[j] + 1)
print(max(d))