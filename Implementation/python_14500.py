# 테트로미노

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        # 일자형 가로
        if j + 3 < m:
            total = 0
            for k in range(4):
                total += paper[i][j + k]
            result = max(result, total)
        # 일자형 세로
        if i + 3 < n:
            total = 0
            for k in range(4):
                total += paper[i + k][j]
            result = max(result, total)
        
        # L자형 가로
        if j + 2 < m:
            total = 0
            tmp1 = 0
            tmp2 = 0
            tmp3 = 0
            tmp4 = 0
            for k in range(3):
                total += paper[i][j + k]
            if i + 1 < n:
                tmp1 = paper[i + 1][j + 2]
                tmp3 = paper[i + 1][j]
            if i - 1 >= 0:
                tmp2 = paper[i - 1][j + 2]
                tmp4 = paper[i - 1][j]
            result = max(result, total + max(tmp1, tmp2, tmp3, tmp4))
        # L자형 세로
        if i + 2 < n:
            total = 0
            tmp1 = 0
            tmp2 = 0
            tmp3 = 0
            tmp4 = 0
            for k in range(3):
                total += paper[i + k][j]
            if j + 1 < m:
                tmp1 = paper[i + 2][j + 1]
                tmp3 = paper[i][j + 1]
            if j - 1 >= 0:
                tmp2 = paper[i + 2][j - 1]
                tmp4 = paper[i][j - 1]
            result = max(result, total + max(tmp1, tmp2, tmp3, tmp4))
        
        # 사각형
        if i + 1 < n and j + 1 < m:
            total = paper[i][j] + paper[i + 1][j] + paper[i + 1][j + 1] + paper[i][j + 1]
            result = max(total, result)
        
        # ㅜ자형 - 가로
        if j + 2 < m:
            total = 0
            tmp1 = 0
            tmp2 = 0
            for k in range(3):
                total += paper[i][j + k]
            if i + 1 < n:
                tmp1 = paper[i + 1][j + 1]
            if i - 1 >= 0:
                tmp2 = paper[i - 1][j + 1]
            result = max(result, total + max(tmp1, tmp2))
        # ㅜ자형 - 세로
        if i + 2 < n:
            total = 0
            tmp1 = 0
            tmp2 = 0
            for k in range(3):
                total += paper[i + k][j]
            if j + 1 < m:
                tmp1 = paper[i + 1][j + 1]
            if j - 1 >= 0:
                tmp2 = paper[i + 1][j - 1]
            result = max(result, total + max(tmp1, tmp2))

        # 꺾인형 - 가로
        if j + 2 < m:
            total = 0
            tmp1 = 0
            tmp2 = 0
            for k in range(2):
                total += paper[i][j + k]
            if i + 1 < n:
                tmp1 = paper[i + 1][j + 1] + paper[i + 1][j + 2]
            if i - 1 >= 0:
                tmp2 = paper[i - 1][j + 1] + paper[i - 1][j + 2]
            result = max(result, total + max(tmp1, tmp2))

        # 꺾인형 - 세로
        if i + 2 < n: #i == 1 j == 3
            total = 0
            tmp1 = 0
            tmp2 = 0
            for k in range(2):
                total += paper[i + k][j]
            if j + 1 < m:
                tmp1 = paper[i + 1][j + 1] + paper[i + 2][j + 1]
            if j - 1 >= 0:
                tmp2 = paper[i + 1][j - 1] + paper[i + 2][j - 1]
            result = max(result, total + max(tmp1, tmp2))

print(result)