# 2차 답안 (딕셔너리 이용)
def solution(id_list, report, k):
    report = list(set(report))
    check = {}
    answer= []
    
    for i in id_list:
        check[i] = []
        answer.append(0)
    
    for i in report:
        user, reported = i.split()
        
        if reported in id_list:
            check[reported].append(user)

    for i in range(len(id_list)):
        user_list = check.get(id_list[i])
        if len(user_list) >= k:
            for j in user_list:
                answer[id_list.index(j)] += 1
    
    return answer

# 1차 답안
# def solution(id_list, report, k):
    
#     id_num = len(id_list)
#     report_num = len(report)
#     result = []
#     answer = []
#     report_list = []
    
#     for i in range(id_num):
#         result.append([])
#         answer.append(0)
        
    
#     for i in range(report_num):
#         report_list.append([])
#         a, b = report[i].split()
#         report_list[i].append(a)
#         report_list[i].append(b)
        
#     for i in range(report_num):
#         for j in range(id_num):
#             if id_list[j] == report_list[i][1]:
#                 result[j].append(report_list[i][0])
#             result[j] = list(set(result[j]))
    
    
#     for i in range(id_num):
#         if len(result[i]) >= k:
#             for j in range(id_num):
#                 if id_list[j] in result[i]:
#                     answer[j] += 1
        
#     return answer