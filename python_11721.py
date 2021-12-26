#  한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.

word = input()

for i in range(len(word)):
    if i == 0:
        print(word[i], end="")
    elif (i + 1) % 10 == 0 :
        print(word[i])
    else:
        print(word[i], end="")
        