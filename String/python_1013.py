# Contact

import re

n = int(input())

for _ in range(n):
    word = input()
    result = re.compile('(100+1+|01)+')
    if result.fullmatch(word):
        print('YES')
    else:
        print('NO')