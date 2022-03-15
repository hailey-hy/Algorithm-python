# 카드 2

from collections import deque
import sys
n = int(sys.stdin.readline())

cards = deque([])
for i in range(1, n + 1):
    cards.append(i)

while len(cards) > 1:
    cards.popleft()
    cards.append(cards[0])
    cards.popleft()

print(cards[0])