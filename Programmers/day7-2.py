# 오픈채팅방

def solution(record):
    answer = []
    in_out = dict()
    for i in record:
        if 'Enter' in i:
            a, user_id, user_nick = i.split()
            in_out[user_id] = user_nick
            answer.append(user_id + ' in')
        elif 'Change' in i:
            a, user_id, user_nick = i.split()
            in_out[user_id] = user_nick
        else:
            a, user_id = i.split()
            answer.append(user_id + ' out')
    
    msg = []
    for i in answer:
        user_id, where = i.split()
        if where == 'in':
            msg.append(in_out[user_id] + '님이 들어왔습니다.')
        else:
            msg.append(in_out[user_id] + '님이 나갔습니다.')
            
    return msg