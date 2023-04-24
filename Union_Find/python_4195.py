# 친구 네트워크

import sys

def find_parent(x):
    global parent
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def uinon_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
        return a, b
    else:
        parent[a] = b
        return b, a

def same_parent(a, b):
    return find_parent(a) == find_parent(b)

t = int(sys.stdin.readline())
for i in range(t):
    f = int(sys.stdin.readline())
    friends = dict()
    total = 0
    graph = []
    for _ in range(f):
        x, y = sys.stdin.readline().rstrip().split()
        if x not in friends:
            total += 1
            friends[x] = total
        if y not in friends:
            total += 1
            friends[y] = total
        graph.append((friends[x], friends[y]))

    parent = [i for i in range(total + 1)]
    counted = [1 for _ in range(total + 1)]
 
    for a, b in graph:
        parent_a = find_parent(a)
        parent_b = find_parent(b)
        if not parent_a == parent_b:
            p, c = uinon_parent(a, b)
            print(counted[p] + counted[c])
            counted[p] += counted[c]
        else:
            print(counted[parent_a])