# 소트인사이드

input = input()
num = []
for i in input:
    num.append(int(i))

num.sort(reverse=True)

for i in num:
    print(i, end="")