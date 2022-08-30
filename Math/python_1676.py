# 팩토리얼 0의 개수

n = int(input())

num = 1
for i in range(n, 1, -1):
    num *= i

num_word = [i for i in str(num)]

answer = 0
for i in range(len(num_word)):
    if num_word[-1] == "0":
        answer += 1
        num_word.pop(-1)

print(answer)