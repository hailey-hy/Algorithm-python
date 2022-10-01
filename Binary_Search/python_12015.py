# 가장 긴 증가하는 부분 수열 2

n = int(input())
array = [0] + list(map(int, input().split()))

cnt = 0
memo = [0]

for case in array:
    if memo[-1] < case:
        memo.append(case)
    else:
        left = 0
        right = len(memo)

        while left < right:
            mid = (left + right) // 2

            if memo[mid] < case:
                left = mid + 1
            else:
                right = mid
        
        memo[right] = case

print(len(memo) - 1)