#소수 2
min = int(input())
max = int(input())
prime = []
for i in range(min, max + 1):
    checker = 0
    for j in range(2, i):
        if i % j == 0:
            checker += 1
            break
    if checker == 0 and i > 1:
        prime.append(i)
if len(prime) == 0:
    print(-1)
else:
    print(sum(prime))
    print(prime[0])