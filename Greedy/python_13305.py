# 주유소

n = int(input())

roads = list(map(int, input().split()))
cities = list(list(map(int, input().split())))

price = cities[0]
fuel = 0

for i in range(n - 1):
    if cities[i] <= price:
        price = cities[i]
    fuel += price * roads[i]

print(fuel)
