# 가장 긴 바이토닉 부분 수열

n = int(input())
array = list(map(int, input().split()))

d_increase = [1] * (n + 1)
d_decrease = [1] * (n + 1)
d_bitonic = [0] * (n + 1)

for i in range(n):
    for j in range(i):
        if array[j] < array[i]:
            d_increase[i] = max(d_increase[i], d_increase[j] + 1)
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if array[j] < array[i]:
            d_decrease[i] = max(d_decrease[i], d_decrease[j] + 1)
for i in range(n):
    d_bitonic[i] = d_increase[i] + d_decrease[i] - 1
print(max(d_bitonic))