# 나는야 포켓몬 마스터 이다솜

import sys

n, m = map(int, sys.stdin.readline().split())

pokemons = dict()
questions = []

for i in range(n):
    pokemons[i] = sys.stdin.readline().strip()

re_pokemons = dict(map(reversed, pokemons.items()))

for i in range(m):
    questions.append(sys.stdin.readline().strip())

for i in questions:
    if i.isdigit():
        print(pokemons[int(i) - 1])
    else:
        print(re_pokemons.get(i) + 1)

