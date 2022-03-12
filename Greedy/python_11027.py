# 동전 0
import sys

n, total = map(int, sys.stdin.readline().split())

coins = []
value = 0

for i in range(n):
    coins.append(int(sys.stdin.readline()))

while total > 0:
    if coins[-1] > total:
        coins.pop()
    elif coins[-1] <= total:
        value += 1
        total -= coins[-1]

print(value)

# 좋은 풀이(@secrett2633)
n, k = input().split(" ")
n = int(n)
k = int(k)
price = []
sum = 0
for i in range(n):
    price.append(int(input()))
price.reverse()
for i in price:
    sum += k//i
    k = k%i
print(sum)