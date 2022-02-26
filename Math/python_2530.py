# 인공지능 시계

h, m , s = map(int, input().split())
seconds = int(input())

s += seconds

while(True):
    if s < 60:
        print(h, m, s)
        break
    else:
        m += s // 60
        s %= 60
        
    if m < 60:
        print(h, m, s)
        break
    else:
        h += m // 60
        m %= 60
        
    if h < 24:
        print(h, m, s)
        break
    elif h == 24:
        print(0, m, s)
        break
    else:
        print(h%24, m, s)
        break