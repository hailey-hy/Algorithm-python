# 서로 다른 부분 문자열의 개수

word = input()
subset = dict()
answer = 0

for i in range(1, len(word) + 1):
    made = ''
    for j in range(len(word)):
        made = word[j : j + i]
        if len(made) == i:
            if subset.get(made, False):
                subset[made] = subset[made] + 1
            else:
                subset[made] = 1
        
print(len(subset))