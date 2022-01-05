# 설탕 배달

# 그리디로 푼다면
n = int(input())
cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        break
    else:
        n -= 3
        if n < 0:
            break
        cnt += 1
if n >= 0:
    print(cnt)
else:
    print(-1)

# DP로 푼다면
n = int(input())

d = [5001] * (n + 5)
d[3] = d[5] = 1

for i in range(6, n + 1):
    d[i] = min(d[i - 3], d[i - 5]) + 1

print(d[n] if d[n] < 5001 else -1)