# 124 나라의 숫자

def solution(n):
    power = 0
    tmp = ''
    while n:
        if n % 3 == 0:
            tmp = str(4) + tmp
            n = n // 3 - 1
        else:
            tmp = str(n % 3) + tmp
            n //= 3
    return tmp
