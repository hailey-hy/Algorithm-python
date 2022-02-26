# 좌표 압축

n = int(input())
array = list(map(int, input().split()))

set_sorted = sorted(list(set(array)))

dic = {set_sorted[i] : i for i in range((len(set_sorted)))}

for i in array:
    print(dic[i], end=" ")
