# 회문

import sys

def checkPelin(word):
    start = 0
    end = len(word) - 1
    while start < end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            if word[start:end] == word[start:end][::-1]:
                return 1
            elif word[start + 1:end + 1] == word[start + 1:end + 1][::-1]:
                return 1
            else:
                return 2
    return 0

n = int(sys.stdin.readline())
for i in range(n):
    word = list(sys.stdin.readline().rstrip())
    print(checkPelin(word))
    
