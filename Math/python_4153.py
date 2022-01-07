# 직각삼각형

while True:
    array = list(map(int, input().split()))
    if sum(array) == 0:
        break
    array.sort()
    if array[2] ** 2 == array[0] ** 2 + array[1] ** 2:
        print("right")
    else:
        print("wrong")
