# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와 살아야할 경우,
# 각각의 Test case에 대해 해당 집의 거주민 수를 출력하라

case_num = int(input())


for i in range(case_num): 
    ground_floor = []
    floor = int(input())
    room = int(input())
    for j in range(1, room + 1): 
        ground_floor.append(j)
    for j in range(1, floor + 1): 
        for k in range(1, room):
            ground_floor[k] += ground_floor[k - 1]
    print(ground_floor[room - 1])
