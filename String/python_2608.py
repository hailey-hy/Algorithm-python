# 로마 숫자

from collections import deque

loma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
decimal = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
answer = 0

def to_decimal(x):
    stack = deque([])
    total = 0
    for i in x:
        if len(stack) > 0:
            if loma[stack[0]] == loma[i]:
                stack.appendleft(i)
            elif loma[stack[0]] > loma[i]:
                total += loma[stack[0]] * len(stack)
                stack = deque([])
                stack.append(i)
            else:
                total += loma[i] - loma[stack[0]]
                stack.pop()
        else:
            stack.append(i)
    for i in stack:
        total += loma[i]
    return total

def to_loma(x):
    answer = ''
    for i in range(len(x)):
        now = int(x[i]) * 10 ** (len(x) - i - 1)
        if now in [4, 9, 40, 90, 400, 900]:
            stack = deque([])
            tmp = 0
            for j in decimal.keys():
                if abs(now - j) < abs(now - tmp):
                    tmp = j
            stack.append(decimal[tmp])
            for j in decimal.keys():
                if loma[stack[0]] - j == now:
                    stack.appendleft(decimal[j])
                    break
            for j in stack:
                answer += j
        elif int(x[i]) in [6, 7, 8]:
            tmp = 0
            for j in decimal.keys():
                if now > j:
                    tmp = j
            answer += decimal[tmp]
            now -= tmp
            tmp = 0
            for j in decimal.keys():
                if 10 ** (len(x) - i - 1) == j:
                    tmp = j
            for j in range(int(x[i]) - 5):
                answer += decimal[tmp]
        elif int(x[i]) == 5:
            tmp = 0
            for j in decimal.keys():
                if now == j:
                    tmp = j
            answer += decimal[tmp]
        else:
            tmp = 0
            for j in decimal.keys():
                if 10 ** (len(x) - i - 1) == j:
                    tmp = j
            for j in range(int(x[i])):
                answer += decimal[tmp]
    return answer
        
for _ in range(2):
    answer += to_decimal(list(input()))

print(answer)
print(to_loma(str(answer)))