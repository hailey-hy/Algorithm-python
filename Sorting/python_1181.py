# 단어 정렬

n = int(input())
words = []

for i in range(n):
    words.append(input())

words = list(set(words))

words.sort(key=lambda x: ascii(x))
words.sort(key=len)

for j in words:
    print(j)