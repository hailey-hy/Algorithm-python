# 이동하기

n, m = map(int, input().split())

maze = []

for i in range(n):
    maze.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            continue
        elif i == 0 and j >= 1:
            maze[i][j] += maze[i][j - 1]
        elif i >= 1 and j == 0:
            maze[i][j] += maze[i - 1][j]
        else:
            maze[i][j] += max(maze[i - 1][j], maze[i][j - 1], maze[i - 1][j - 1])

print(maze[n - 1][m - 1])