# 단어 맞추기

def nextPermutation(arr):
    i = len(arr) - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1
    if i == -1:
        return False
    
    j = len(arr) - 1
    while arr[i] >= arr[j]:
        j -= 1
    
    arr[i], arr[j] = arr[j], arr[i]
    result = arr[:i + 1]
    result.extend(list(reversed(arr[i + 1:])))
    return result

t = int(input())
for _ in range(t):
    word = list(input())
    answer = nextPermutation(word)
    if not answer:
        print(''.join(word))
    else:
        print(''.join(answer))
    
    
    