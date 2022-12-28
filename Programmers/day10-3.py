# 귤 고르기

def solution(k, tangerine):
    dic = dict()
    for i in tangerine:
        if str(i) in dic:
            dic[str(i)] += 1
        else:
            dic[str(i)] = 1
    
    new_dic = dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))

    answer = 0

    for key, value in new_dic.items():
        k -= value
        answer += 1
        if k <= 0:
            return answer