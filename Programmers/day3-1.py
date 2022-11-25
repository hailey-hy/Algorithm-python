# 카펫

def solution(brown, yellow):
    answer = [0, 0]
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            x = i
            y = yellow // i
            if x * 2 + y * 2 + 4 == brown:
                answer[0] = x + 2
                answer[1] = y + 2
    
    return answer