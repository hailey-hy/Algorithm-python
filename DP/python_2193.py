# 이친수

n = int(input())

d = [1] * (n)

for i in range(2, n):
    if n <= 1:
        break
    d[i] = d[i - 1] + d[i - 2]

print(d[n - 1])
    
