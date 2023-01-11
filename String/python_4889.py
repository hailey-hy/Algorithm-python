# 안정적인 문자열

index = 1
while True:
    case = list(input())
    if '-' in case:
        break
    stack = []
    answer = 0
    for i in case:
        if i == '{':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer += 1
                stack.append('{')
    while stack:
        if len(stack) % 2 == 0:
            answer += 1
        stack.pop()
    print(str(index) + '. ' + str(answer))
    index += 1