# 최소공배수

t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    deno = 1
    for j in range(1, a + 1):
        if a % j == 0 and b % j == 0:
            deno = j
    print(a * b // deno)