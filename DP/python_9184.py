# 신나는 재귀 함수

d = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b >20 or c > 20:
        return w(20,20,20)
    if d[a][b][c] != 0:
        return d[a][b][c]
    elif a < b and b < c:
        d[a][b][c] = (w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c))
        return d[a][b][c]
    else:
        d[a][b][c] = (w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1))
        return d[a][b][c]
    

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
