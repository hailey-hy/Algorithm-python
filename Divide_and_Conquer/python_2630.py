# 색종이 만들기

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

white_all = 0
blue_all = 0

def cut(x, y, z): #0 8 8
    for i in range(x, z):
        for j in range(x, y):
            
    cut_n = y // 2
    cut(x, cut_n, cut_n)
    cut(x, cut_n, y)
    cut(cut_n, cut_n, y)
    cut(cut_n, y, z)



# n = int(input())
# paper = []

# for _ in range(n):
#     paper.append(list(map(int,input().split())))

# white = 0
# blue = 0

# def cut(row, col, n):
#     global white, blue

#     curr = paper[row][col]
#     for i in range(row, row + n):
#         for j in range(col, col + n):
#             if curr != paper[i][j]:
#                 next_n = n // 2
#                 cut(row, col, next_n)
#                 cut(row, col + next_n, next_n)
#                 cut(row + next_n, col, next_n)
#                 cut(row + next_n, col + next_n, next_n)
#                 return

#     if curr == 0:
#         white += 1
#     else:
#         blue += 1
#     return

# cut(0, 0, n)
# print(white)
# print(blue)