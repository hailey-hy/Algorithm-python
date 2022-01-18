# 소수 찾기
n = int(input())
array = list(map(int, input().split()))

prime_num = 0
for i in array:
    prime_cnt = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            prime_cnt += 1
    if prime_cnt == 0:
        prime_num += 1
            
print(prime_num)