# 회의실 배정

n = int(input())

rooms = []
for i in range(n):
    rooms.append(list(map(int, input().split())))

rooms.sort(key= lambda x:x[0])
rooms.sort(key= lambda x:x[1])

end = 0
count = 0

for i, j in rooms:
    if i >= end:
        count += 1
        end = j

print(count)