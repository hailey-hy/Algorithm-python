# 택시 기하학


import math

n = int(input())

print("{0:6f}".format(round(math.pi * (n ** 2), 6)))

circle = math.sqrt(((n ** 2) * 2)) ** 2

print("{0:6f}".format(round(circle, 6)))