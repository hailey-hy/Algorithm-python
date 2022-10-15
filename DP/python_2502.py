# 떡 먹는 호랑이

day, dduk = map(int, input().split())

a, b = 1, 1

for i in range(3, day):
    a, b = b, a + b
    
ac = 1
bc = 0

while True:
    tmp = dduk - a * ac
    if tmp < 0:
        break

    if tmp % b == 0:
        bc = tmp // b
        break

    ac += 1

print(ac)
print(bc)