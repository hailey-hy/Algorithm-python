# 나만 안되는 연애

n, m = map(int, input().split())
gender_tmp = list(input().split())
gender = {}
for i in range(n):
    gender[i + 1] = gender_tmp[i]
graph = []

for _ in range(m):
    u, v, d = map(int, input().split())
    graph.append((u, v, d))

graph.sort(key= lambda x:x[2])
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
count = 0
tmp = ''
for a, b, cost in graph:
    if not same_parent(a, b):
        if gender[a] != gender[b]:
            union_parent(a, b)
            answer += cost
            count += 1
            tmp = gender[b]
        if answer == n - 1:
            break
if count != n - 1:
    answer = -1
print(answer)