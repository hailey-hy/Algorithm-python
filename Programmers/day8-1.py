# 주식 가격

from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        now = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if i < now:
                break

        answer.append(cnt)

    return answer