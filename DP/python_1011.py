# Fly me to the Alpha Centauri

n = int(input())
array = []
for i in range(n):
    x, y = map(int, input().split())
    array.append(y - x + 1)

d = []

for i in range(2):
    d.append(0)

d.append(1)

for l in range(2, max(array) + 1):
    for j in range(l - 1):
        d.append(l)

for k in range(n):
    print(d[array[k]])