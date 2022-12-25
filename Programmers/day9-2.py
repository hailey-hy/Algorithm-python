# 소수 찾기

from itertools import permutations
import math

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    possibles = []
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):
                possibles.append(int(''.join(j)))
                
    possibles = list(set(possibles))
    for i in possibles:
        if isPrime(i):
            answer += 1
    
    return answer