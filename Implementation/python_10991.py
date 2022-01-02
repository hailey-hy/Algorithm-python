#별 찍기

n = int(input())

for i in range(1, n + 1):
    if i == 1:
        print(" " * (n - i) + "*")
    elif i == n:
        print("* " * (n - 1) + "*")
    else:
        print(" " * (n - i - 1) + " *" * i)