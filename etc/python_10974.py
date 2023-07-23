# 모든 순열

from itertools import permutations

n = int(input())
n_permutation = list(permutations(range(1, n + 1), n))

for answer in n_permutation:
    print(*answer)
