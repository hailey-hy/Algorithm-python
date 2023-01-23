# 알파벳

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bfs():
    q = set([(0, 0, board[0][0])])
    visited = [[''] * m for _ in range(n)]
    visited[0][0] = board[0][0]
    total = 1
    while q:
        x, y, record = q.pop()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if 0 <= new_x < n and 0 <= new_y < m and board[new_x][new_y] not in record:
                    new_record = record + board[new_x][new_y]
                    visited[new_x][new_y] = new_record
                    q.add((new_x, new_y, new_record))
                    total = max(total, len(visited[new_x][new_y]))
    
    return total

print(bfs())

