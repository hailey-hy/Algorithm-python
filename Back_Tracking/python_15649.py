# N과 M 1
def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
        
    for i in range(1, n + 1):
        if i in stack:
            continue
        stack.append(i)
        dfs()
        stack.pop()

n, m = map(int, input().split())
stack = []
dfs()