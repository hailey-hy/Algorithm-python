# 베르트랑 공준

import math
def isprime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

array = list(range(2, 246912))
prime = []
for i in array:
    if isprime(i):
        prime.append(i)

n = int(input())

while(n != 0):
    cnt = 0
    for i in prime:
        if n < i <= 2 * n:
            cnt += 1
    print(cnt)
    n = int(input())