# 피보나치 함수


n = int(input())

for i in range(n):
    num = int(input())
    zero = 1
    one = 0
    cnt = 0
    for _ in range(num):
        cnt = one
        one = one + zero
        zero = cnt
    print(zero, one)
