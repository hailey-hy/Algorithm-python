# k진수에서 소수 개수 구하기

import math

def solution(n, k):
    answer = 0
    
    def is_prime(n): 
        if n == 1:
            return False
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                return False
        return True
    
    changed = ''
    while n:
        changed = str(n % k) + changed
        n //= k
        
    n_list = [i for i in changed.split('0')]
    n_list = list(map(int, ' '.join(n_list).split()))
    
    print(n_list)
    for i in n_list:
        if i != "" and i != "1" and is_prime(int(i)):
            answer += 1

    return answer