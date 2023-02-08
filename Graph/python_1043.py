# 거짓말

n, m = map(int, input().split())
truth = set(input().split()[1:])
parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

cnt = 0
for party in parties:
    if party & truth:
        continue
    cnt += 1

print(cnt)