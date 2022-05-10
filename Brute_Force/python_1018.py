# 체스판 다시 칠하기

y, x = map(int, input().split())
board = []

for i in range(y):
    board.append(list(input()))

paint = [0, 0]

for i in range(y): #WB패턴: 0 BW패턴: 1
    for j in range(x):
        if (i == 0 or i % 2 == 0) and (j == 0 or j % 2 == 0) and (board[i][j] != "W"):
            paint[0] += 1
        if (i == 0 or i % 2 == 0) and (j % 2 != 0) and (board[i][j] != "B"):
            paint[0] += 1            
        if (i == 0 or i % 2 == 0) and (j == 0 or j % 2 == 0) and (board[i][j] != "B"):
            paint[1] += 1
        if (i == 0 or i % 2 == 0) and (j % 2 != 0) and (board[i][j] != "W"):
            paint[1] += 1  
        if (i % 2 != 0) and (j % 2 != 0) and (board[i][j] != "W"):
            paint[0] += 1
        if (i % 2 != 0) and (j == 0 or j % 2 == 0) and (board[i][j] != "B"):
            paint[0] += 1
        if (i % 2 != 0) and (j % 2 != 0) and (board[i][j] != "B"):
            paint[1] += 1
        if (i % 2 != 0) and (j == 0 or j % 2 == 0) and (board[i][j] != "W"):
            paint[1] += 1


print(min(paint))