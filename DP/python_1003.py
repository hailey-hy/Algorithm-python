# 피보나치 함수


n = int(input())

d_0 = [1, 0]
d_1 = [0, 1]



for i in range(n):
    num = int(input())
    for j in range(2, num + 1):
        d_0.append(d_0[j - 2] + d_0[j - 1])
        d_1.append(d_1[j - 2] + d_1[j - 1])
    print(d_0[num], d_1[num])
