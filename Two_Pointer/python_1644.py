# 소수의 연속합

import sys
import math

n = int(sys.stdin.readline())

def prime_number(x):
    prime = [True] * (x + 1)
    for i in range(2, int(math.sqrt(x)) + 1):
        if prime[i]:
            j = 2
            while i * j <= n:
                prime[i * j] = False
                j += 1
            
    return prime

prime = prime_number(n)
numbers = []
for i in range(2, n + 1):
    if prime[i]:
        numbers.append(i)

def two_pointer():
    result = 0
    start = 0
    end = 0
    length = len(numbers)

    tmp = numbers[start]
    while start <= end:
        if tmp < n:
            end += 1
            if end >= length:
                break
            tmp += numbers[end]
        elif tmp > n:
            tmp -= numbers[start]
            start += 1
            if start >= length:
                break
        else:
            result += 1
            end += 1
            if end >= length:
                break
            tmp += numbers[end]
    return result

if n > 1:
    print(two_pointer())
else:
    print(0)