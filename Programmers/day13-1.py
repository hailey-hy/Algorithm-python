# 방문 길이

from collections import deque

def solution(dirs):
    answer = 0
    
    dx = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
    dy = {'U': 0, 'D': 0, 'L': -1, 'R': 1}
    directions = {'U': 3, 'D': 2, 'L': 1, 'R': 0} #동서남북
    reverse = {'U': 2, 'D': 3, 'L': 0, 'R': 1}
    
    visited = [[[False, False, False, False] for i in range(11)] for j in range(11)]
    x, y = 5, 5
    for i in dirs:
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < 11 and 0 <= new_y < 11:
            if not visited[new_x][new_y][reverse[i]] and not visited[x][y][directions[i]]:
                visited[x][y][directions[i]] = True
                visited[new_x][new_y][reverse[i]] = True
                answer += 1
            x = new_x
            y = new_y
                
                
    return answer