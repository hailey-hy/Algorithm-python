# 정수 삼각형

array = []
n = int(input())

for i in range(n):
    array.append(list(map(int, input().split())))

cnt = 2

for i in range(1, n):
    for j in range(cnt):
        if j == 0:
            array[i][j] = array[i][j] + array[i - 1][j]
        elif i == j:
            array[i][j] = array[i][j] + array[i - 1][j - 1]
        else:
            array[i][j] = array[i][j] + max(array[i - 1][j], array[i - 1][j - 1])
    cnt += 1

print(max(array[n - 1]))