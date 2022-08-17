# 배수와 약수

first, second = map(int, input().split())

while first != 0:
    if second % first == 0:
        print("factor")
    elif first % second == 0:
        print("multiple")
    else:
        print("neither")
        
    first, second = map(int, input().split())