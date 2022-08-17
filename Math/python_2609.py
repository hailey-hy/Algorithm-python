# 최대공약수와 최소공배수

a, b = map(int, input().split())
deno = 0

for i in range(1, a // 2 + 1):
    if a % i == 0 and b % i == 0:
        deno = i

print(deno)
print(a * b // deno)