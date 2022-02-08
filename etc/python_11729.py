# 하노이의 탑

n = int(input())

def hanoi(n, start, middle, end):
    if n == 1:
        print(start, end)
    else:
        hanoi(n - 1, start, end, middle)
        print(start, end)
        hanoi(n - 1, middle, start, end)
sum = 1
for i in range(n - 1):
    sum = sum * 2 + 1
print(sum)
hanoi(n, 1, 2, 3)