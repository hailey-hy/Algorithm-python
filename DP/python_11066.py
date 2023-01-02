# 파일 합치기

t = int(input())
for i in range(t):
    k = int(input())
    files = list(map(int, input().split()))
    minCost = [[0] * k for _ in range(k)]

    subSum = {-1 : 0}
    for idx in range(k):
        subSum[idx] = subSum[idx - 1] + files[idx]
    
    for size in range(1, k):
        for start in range(k - 1):
            end = start + size
            if end >= len(files):
                break
            result = float("inf")
            for cut in range(start, end):
                result = min(result, minCost[start][cut] + minCost[cut + 1][end] + subSum[end] - subSum[start - 1])

            minCost[start][end] = result

print(minCost[0][-1])