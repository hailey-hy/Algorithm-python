# 네 번째 점

x = []
y = []

for i in range(3):
    temp = list(map(int, input().split()))
    x.append(temp[0])
    y.append(temp[1])

for i in x:
    if x.count(i) == 1:
        print(i, end=" ")

for i in y:
    if y.count(i) == 1:
        print(i)