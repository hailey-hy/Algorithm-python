# 공유기 설치

n, c = map(int, input().split())
houses = []

for _ in range(n):
    houses.append(int(input()))

houses.sort()

start, end = 1, houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    current = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if houses[i] - current >= mid:
            count += 1
            current = houses[i]
        
        if count >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

print(answer)