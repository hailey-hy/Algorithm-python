# 한줄로 서기

n = int(input())
people = list(map(int, input().split()))
info = [-1] * n
for i in range(n):
    for j in range(n):
        tmp = 0
        for k in info[0:j]:
            if k > i + 1 or k == -1:
                tmp += 1
        if tmp == people[i] and info[j] == -1:
            info[j] = i + 1
            break

print(' '.join(map(str, info)))
# 8 4 7 2 6 1 9 5 10 3
