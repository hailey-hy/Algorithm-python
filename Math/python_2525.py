# 오븐 시계

hour, minute = map(int, input().split())
time = int(input())

if minute + time >= 60:
    hour += (minute + time) // 60
    minute = (minute + time) % 60
else:
    minute += time

if hour >= 24:
    hour %= 24

print(hour, minute)
