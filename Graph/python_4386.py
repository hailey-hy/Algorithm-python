# 별자리 만들기

n = int(input())
tmp = []
for _ in range(n):
    tmp.append(list(map(float, input().split())))

graph = []
for i in range(n):
    for j in range(n):
        if not i == j:
            distance = (tmp[i][0] - tmp[j][0]) ** 2 + (tmp[i][1] - tmp[j][1]) ** 2
            graph.append((i, j, distance ** (1/2)))

graph.sort(key=lambda x:x[2])

parent = [i for i in range(n + 1)]
def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in graph:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost

print(round(answer, 2))