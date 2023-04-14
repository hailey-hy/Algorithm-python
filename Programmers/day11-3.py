# 뒤에 있는 큰 수 찾기

def solution(numbers):
    n = len(numbers)
    result = [-1] * n
    stack = []

    stack.append(0)
    for i in range(1, n):
        while stack and numbers[stack[-1]] < numbers[i]:
            
            result[stack.pop()] = numbers[i]
        stack.append(i)
        
    return result