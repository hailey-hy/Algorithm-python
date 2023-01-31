# 배열 탈출

# 다익스트라 (시간 초과)
# import sys
# import heapq

# n = int(sys.stdin.readline())
# array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# memo = [[sys.maxsize] * n for _ in range(n)]
# dx = [0, 1]
# dy = [1, 0]

# def dijkstra(x, y):
#     q = []
#     heapq.heappush(q, (0, x, y))
#     memo[x][y] = 0
#     while q:
#         now_cost, now_x, now_y = heapq.heappop(q)

#         if memo[now_x][now_y] < now_cost:
#             continue

#         for i in range(2):
#             new_x = now_x + dx[i]
#             new_y = now_y + dy[i]
#             if 0 <= new_x < n and 0 <= new_y < n:
#                 if array[new_x][new_y] >= array[now_x][now_y]:
#                     tmp_cost = array[new_x][new_y] - array[now_x][now_y] + 1
#                 else:
#                     tmp_cost = 0
#                 new_cost = now_cost + tmp_cost
#                 if new_cost < memo[new_x][new_y]:
#                     memo[new_x][new_y] = new_cost
#                     heapq.heappush(q, (new_cost, new_x, new_y))

# dijkstra(0, 0)
# print(memo[n - 1][n - 1])