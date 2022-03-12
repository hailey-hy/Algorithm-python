# 스택 수열

n = int(input())
stack = []
result = []
count = 1
temp = True

for i in range(n):
    number = int(input())
    while count <= number:
        stack.append(count)
        result.append("+")
        count += 1
    if stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        temp = False
if temp == False:
    print("NO")
else:
    for i in result:
        print(i)
