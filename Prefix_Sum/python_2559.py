# 수열

n, k = map(int, input().split())

temps = list(map(int, input().split()))
temps_sum = [0]

for i in range(n):
    temps_sum.append(temps_sum[i] + temps[i])

max_num = 0

if k == n:
    print(temps_sum[-1])

else:
    for i in range(n - k + 1):
        if temps_sum[i + k] - temps_sum[i] >= max_num:
            max_num = temps_sum[i + k] - temps_sum[i]

    print(max_num)