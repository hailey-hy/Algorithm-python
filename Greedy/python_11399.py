# ATM

n = int(input())
people = list(map(int, input().split()))

people.sort()
time = 0
total = 0

for i in people:
    time += i
    total += time

print(total)