# 주어진 날짜의 요일 알아내기

import datetime

A, B = map(int, input().split())

d = datetime.datetime(2007, A, B).strftime("%a")
print(d.upper())
