# 커트라인

n, k = map(int, input().split())

print(sorted(list(map(int, input().split())))[n - k])