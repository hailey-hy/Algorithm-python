# 잃어버린 괄호

word = input()
length = len(word)
cnt = 0
problem = []
num = ""

for i in range(length):
    if word[i] == "-":
        cnt += 1
        if cnt == 1:
            problem.append(int(num))
            problem.append(word[i])
            problem.append("(")
            num = ""
        elif cnt == word.count("-"):
            problem.append(int(num))
            problem.append(")")
            problem.append(word[i])
            problem.append("(")
            num = ""
        else:
            problem.append(int(num))
            problem.append(")")
            problem.append(word[i])
            problem.append("(")
            num = ""
    elif word[i] == "+":
        problem.append(int(num))
        problem.append(word[i])
        num = ""
    elif i == length - 1:
        num += word[i]
        problem.append(int(num))
        if problem.count("(") >= 1:
            problem.append(")")
    else:
        num += word[i]

num = ""

for i in problem:
    num += str(i)

print(eval(num))

# 다른 풀이 @experien
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
print(e)
