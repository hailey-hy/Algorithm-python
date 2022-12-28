# n진수 게임

def change(n, toWhat):
    result = ''
    convertString = '0123456789ABCDEF'
    while n:
        result += convertString[n % toWhat]
        n = n // toWhat
    return result[::-1]

def solution(n, t, m, p):
    answer = ''
    stack = ''
    turn = 0
    number = -1
    while len(answer) < t:
        number += 1
        if number > 0:
            tmp = change(number, n)
        else:
            tmp = '0'
        for i in tmp:
            if turn == m:
                turn = 1
            else:
                turn += 1
            if turn == p:
                answer += i
            if len(answer) == t:
                break
                
    return answer