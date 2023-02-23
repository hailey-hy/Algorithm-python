from collections import deque
import sys

def solution(maps):
    start = [0, 0]
    end = [0, 0]
    lever = [0, 0]
    length = len(maps)
    length_ = len(maps[0])
    
    for i in range(length):
        for j in range(length_):
            if maps[i][j] == 'S':
                start = [i, j]
            elif maps[i][j] == 'E':
                end = [i, j]
            elif maps[i][j] == 'L':
                lever = [i, j]
                
    def bfs(start_x, start_y, end_x, end_y):
        visited = [[sys.maxsize] * length_ for _ in range(length)]
        visited[start_x][start_y] = 0
        q = deque([(start_x, start_y, 0)])
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while q:
            x, y, time = q.popleft()
            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]
                if 0 <= new_x < length and 0 <= new_y < length_:
                    new_time = time + 1
                    if maps[new_x][new_y] != 'X' and visited[new_x][new_y] > new_time:
                        visited[new_x][new_y] = new_time
                        q.append((new_x, new_y, new_time))
                        
        return visited[end_x][end_y]
    
    to_lever = bfs(start[0], start[1], lever[0], lever[1])
    to_end = bfs(lever[0], lever[1], end[0], end[1])
    
    answer = to_lever + to_end
    
    return answer if answer < sys.maxsize else -1