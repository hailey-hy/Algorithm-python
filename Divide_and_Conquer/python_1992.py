# 쿼드트리

n = int(input())
video = []

for i in range(n):
    temp = input()
    video.append([])
    for j in temp:
        video[i].append(int(j))

def division(start_row, start_col, size):
    if size == 1:   # 픽셀 하나일 때 
        print(video[start_row][start_col], end="")
        return
    num = video[start_row][start_col]

    for row in range(start_row, start_row + size):
        for col in range(start_col, start_col + size):
            if num != video[row][col]:
                print("(", end="")
                size //= 2
                division(start_row, start_col, size)
                division(start_row, start_col + size, size)
                division(start_row + size, start_col, size)
                division(start_row + size, start_col + size, size)
                print(")", end="")
                return

    print(video[start_row][start_col], end="")
    return
    
division(0, 0, n)
