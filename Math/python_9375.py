# 패션왕 신해빈

t = int(input())

for i in range(t):
    n = int(input())
    clothes = dict()

    for j in range(n):
        cloth = list(input().split())
        if cloth[1] in clothes:
            clothes[cloth[1]] += 1
        else:
            clothes[cloth[1]] = 1
    
    count = 1
    for k in clothes.keys():
        count *= clothes[k] + 1
    print(count - 1)
    