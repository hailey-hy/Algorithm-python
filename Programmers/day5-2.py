# 압축

from collections import deque

def solution(msg):
    book = dict()
    for i in range(1, 27):
        book[chr(i + 64)] = i
        
    msg = deque([i for i in msg])
    tmp = deque([])
    answer = []
    while msg:
        while msg:
            if len(tmp) == 0 and msg[0] in book:
                tmp.append(msg.popleft())
            elif ''.join(tmp) + msg[0] in book:
                tmp.append(msg.popleft())
            else:
                word = ''.join(tmp) + msg[0]
                book[word] = max(book.values()) + 1
                break
                
        answer.append(book[''.join(tmp)])
        tmp = []
    return answer