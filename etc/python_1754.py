# 듣보잡

n, m = map(int, input().split())

never_heard =  dict()
both = []

for i in range(n):
    never_heard[input()] = 1

for i in range(m):
    name = input()
    if never_heard.get(name, False):
        never_heard[name] = never_heard[name] + 1
    else:
        never_heard[name] = 1


for i in never_heard:
    if never_heard.get(i) > 1:
        both.append(i)

both.sort()

print(len(both))
for i in both:
    print(i)