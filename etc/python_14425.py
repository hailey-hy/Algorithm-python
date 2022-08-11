# 문자열 집합

n, m = map(int, input().split())

array_A = dict()
answer = 0

for i in range(n):
    array_A[input()] = 1

for i in range(m):
    word = input()
    if array_A.get(word, False):
        array_A[word] = array_A[word] + 1

for i in array_A:
    if array_A.get(i) >= 2:
        answer += array_A.get(i) - 1

print(answer)