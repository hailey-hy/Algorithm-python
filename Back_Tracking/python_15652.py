# N과 M (4)

def dfs():
    if len(stack) == m:
        print(' '.join(map(str, stack)))
        return
    
    for i in range(1, n + 1):
        if len(stack) >= 1 and stack[-1] > i:
            continue
        stack.append(i)
        dfs()
        stack.pop()

n, m = map(int, input().split())
stack = []
dfs()