# 좌표 정렬하기 2

n = int(input())
dots = []
for i in range(n):
    dots.append(list(map(int, input().split())))

dots.sort(key=lambda x: x[0])
dots.sort(key=lambda x: x[1])


for j in range(n):
    for k in range(2):
        print(dots[j][k], end=" ")
    print("\n", end="")
