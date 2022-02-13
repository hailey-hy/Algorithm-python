# 수 정렬하기

n = int(input())

array = [int(input()) for _ in range(n)]

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[len(array)//2]
    lesser_array, equal_array, greater_array = [], [], []
    for num in array:
        if num < pivot:
            lesser_array.append(num)
        elif num == pivot:
            equal_array.append(num)
        else:
            greater_array.append(num)
    return quick_sort(lesser_array) + equal_array + quick_sort(greater_array)

for i in quick_sort(array):
    print(i)