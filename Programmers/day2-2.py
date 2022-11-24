# 숫자의 표현

def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        tmp = 0
        for j in range(i, n):
            tmp += j
            if tmp == n:
                answer += 1
                break
            elif tmp > n:
                break
                
    return answer