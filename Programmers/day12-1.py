# 할인 행사

import copy

def solution(want, number, discount):
    dic = dict()
    for index, i in enumerate(want):
        dic[i] = number[index]
    total = sum(number)
    
    answer = 0
    for i in range(len(discount) - total + 1):
        tmp = discount[i:i + total]
        dic_tmp = copy.deepcopy(dic)
        for j in tmp:
            if j in dic_tmp:
                dic_tmp[j] -= 1
        if all(0 == k for k in dic_tmp.values()) :
            answer += 1
                
    return answer