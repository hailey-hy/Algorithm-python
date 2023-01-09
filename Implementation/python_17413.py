# 단어 뒤집기 2

from collections import deque

word = input()
length = len(word)
answer = []

front = deque([])
back = deque([])
status = False

for i in range(length):
    if word[i] == '<':
        status = True
        answer.append(''.join(back))
        back = deque([])

    elif word[i] == '>':
        status = False
        front.append(word[i])
        answer.append(''.join(front))
        front = deque([])
        continue
    
    if word[i] == ' ':
        if back:
            back.append(' ')
            answer.append(''.join(back))
            back = deque([])
        else:
            front.append(' ')
            answer.append(''.join(front))
            front = deque([])
        continue

    if status:
        front.append(word[i])
    else:
        back.appendleft(word[i])

if back:
    answer.append(''.join(back))
else:
    answer.append(''.join(front))
    

print(''.join(answer))