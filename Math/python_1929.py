# 소수 구하기 - 에라스토테네스의 체

a, b = map(int, input().split())
b += 1
check = [True] * b

for i in range(2, int(b ** 0.5) + 1):
    if check[i]:
        for j in range(2*i, b, i):
            check[j] = False

for i in range(a, b - 1):
    if i > 1 and check[i] == True:
        print(i)
