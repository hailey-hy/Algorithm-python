# 골드바흐의 추측

import math

def goldbach(n):
    if n < 2:
            return False
    for i in range(2, int(math.sqrt(n)) + 1): 
        if n != i and n % i == 0:
            return False
    return True

array = [True] * 10001
for i in range(10001):
    array[i] = goldbach(i)

T = int(input())
for i in range(T):
    n = int(input())
    for k in range(n//2, 1, -1):
        if array[n - k] == True and array[k] == True:
            print(k, n - k)
            break