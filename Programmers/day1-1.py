def solution(id_list, report, k):
    
    id_num = len(id_list)
    report_num = len(report)
    result = []
    answer = []
    report_list = []
    
    for i in range(id_num):
        result.append([])
        answer.append(0)
        
    
    for i in range(report_num):
        report_list.append([])
        a, b = report[i].split()
        report_list[i].append(a)
        report_list[i].append(b)
        
    for i in range(report_num):
        for j in range(id_num):
            if id_list[j] == report_list[i][1]:
                result[j].append(report_list[i][0])
            result[j] = list(set(result[j]))
    
    
    for i in range(id_num):
        if len(result[i]) >= k:
            for j in range(id_num):
                if id_list[j] in result[i]:
                    answer[j] += 1
        
    return answer