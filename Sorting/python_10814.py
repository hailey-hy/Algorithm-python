# 나이 순 정렬

n = int(input())
members = []

for i in range(n):
    members.append(list(input().split()))

for j in range(n):
    members[j][0] = int(members[j][0])

members.sort(key=lambda x : x[0])

for k in range(n):
    for l in range(2):
        print(members[k][l], end=" ")
    print("\n", end="")