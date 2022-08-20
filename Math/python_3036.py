# 링

n = int(input())

array = list(map(int, input().split()))
x = array[0]

for i in range(1, n):
    if x % array[i] == 0:
        print(str(x//array[i]) + "/" + str(1))
    else:
        for j in range(x, 0, -1):
            if x % j == 0 and array[i] % j == 0:
                print(str(x//j) + "/" + str(array[i]//j))
                break
        # 12/8 