# 블랙잭
from itertools import combinations

n, m = map(int, input().split())

cards = list(map(int, input().split()))

blackjack = set()

for i in combinations(cards, 3):
    if i[0] + i[1] + i[2] <= m:
        blackjack.add(i[0] + i[1] + i[2])

print(max(blackjack))

