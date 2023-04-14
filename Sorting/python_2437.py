# 저울

n = int(input())

scale = list(map(int, input().split()))
scale.sort()

target = 1
for i in scale:
    if target < i:
        break
    target += i
print(target)
