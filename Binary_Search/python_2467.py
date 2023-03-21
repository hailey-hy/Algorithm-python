# 용액

import sys

n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))

start = 0
end = len(liquid) - 1
total = [liquid[start], liquid[end]]

tmp_s = start
tmp_e = end

while tmp_s < tmp_e:
    tmp = abs(liquid[start] + liquid[end])
    if tmp > abs(liquid[tmp_s] + liquid[tmp_e]):
        total = [liquid[tmp_s], liquid[tmp_e]]
        start = tmp_s
        end = tmp_e
    
    if tmp == 0:
        break
    
    if liquid[tmp_s] + liquid[tmp_e] < 0:
        tmp_s += 1
    else:
        tmp_e -= 1

print(*total)
        
