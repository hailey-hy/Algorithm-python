# 분해합

n = int(input())

for i in range(n + 1):
    total = i
    total += sum((map(int, str(i))))
    if total == n:
        print(i)
        break
    if i == n:
        print(0)