a = [i.strip(",") for i in input().split()]
a = list(map(int, a))
b = [j.strip(",") for j in input().split()]
b = list(map(int, b))

for i in b:
    if i in a:
        b.remove(i)

print(b)

# 1001, 1008, 1065, 1085, 1110, 1152, 1157, 1193, 1316, 1330, 1546, 1550, 1712, 2292, 2475, 2562, 2577, 2588, 2675, 2753, 2845, 2884, 2908, 2914, 2941, 3003, 3046, 3052, 4344, 4673, 5337, 5338, 5339, 5522, 5554, 5622, 7287, 8958, 9498, 9653, 9654, 10170, 10171, 10172, 10250, 10430, 10699, 10718, 10757, 10809, 10817, 10869, 10871, 10872, 10926, 10998, 11654, 11942, 14681, 15552, 15596