# 좋다

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
answer = 0

for i in range(n):
    start = 0
    end = n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        elif end == i:
            end -= 1
            continue
        tmp = numbers[start] + numbers[end]
        if tmp == numbers[i]:
            answer += 1
            break
        if tmp < numbers[i]:
            start += 1
        else:
            end -= 1

print(answer)
