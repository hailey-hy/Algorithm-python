# 상자 넣기

n = int(input())

boxes = list(map(int, input().split()))
dp = [1] * (n + 1)

for i in range(1, n):
    tmp = 0
    for j in range(i):
        if boxes[j] < boxes[i]:
            tmp = max(tmp, dp[j]) #조건에 맞을 경우 직접 +1하지 않고 대상의 dp값을 그대로 가져오기
            
    dp[i] = tmp + 1

print(max(dp))