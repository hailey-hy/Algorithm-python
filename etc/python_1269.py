# 대칭 차집합

a, b = map(int, input().split())

set_A = dict()
array_A = list(input().split())
array_B = list(input().split())
answer = 0

for i in range(a):
    set_A[array_A[i]] = 1


for i in array_B:
    if set_A.get(i, False):
        set_A[i] = 2
    else:
        set_A[i] = 1

for i in set_A:
    if set_A[i] == 1:
        answer += 1

print(answer)
