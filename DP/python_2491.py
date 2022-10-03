# 수열

n = int(input())

array = list(map(int, input().split()))

dp_bg = [1] * (n + 1)
dp_sm = [1] * (n + 1)

for i in range(n - 1):
    if array[i] <= array[i + 1]:
        dp_bg[i + 1] = dp_bg[i] + 1
    if array[i] >= array[i + 1]:
        dp_sm[i + 1] = dp_sm[i] + 1
        
print(max(max(dp_bg), max(dp_sm)))