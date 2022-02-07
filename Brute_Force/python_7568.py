# 덩치

n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

length = len(array)
rank = []

for i in range(length):
    score = 1
    for j in range(length):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]:
            score += 1
    rank.append(score)

for i in rank:
    print(i, end=" ")