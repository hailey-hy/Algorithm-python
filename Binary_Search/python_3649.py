# 로봇 프로젝트

import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10 ** 7
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()

        start = 0
        end = n - 1

        tmp_s = start
        tmp_e = end
        answer = 'NO'
        answer_arr = []

        while start < end:
            total = lego[start] + lego[end]
            if total == x:
                answer = 'yes'
                answer_arr.append((abs(lego[start] - lego[end]), lego[start], lego[end]))
            
            if total > x:
                end -= 1
            else:
                start += 1

        if answer == 'yes':
            answer_arr.sort(key=lambda x:x[0], reverse=True)
            print(answer, answer_arr[0][1], answer_arr[0][2])
        else:
            print('danger')
    except:
        break