# N과 M (3)

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for i in range(1, n + 1):
        stack.append(i)
        dfs()
        stack.pop()

n, m = map(int, input().split())
stack = []
dfs()