# 이진 변환 반복하기

def solution(s):
    answer = [0, 0]
    while s != "1":
        temp = []
        for i in range(len(s)):
            if s[i] == '1':
                temp.append(s[i])
            else:
                answer[1] += 1
        s = bin(len(''.join(temp)))[2:]
        answer[0] += 1

    return answer