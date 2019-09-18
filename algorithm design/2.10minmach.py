import random
import numpy
import math
import time
import matplotlib.pyplot as plt

# 分治法求解最近点对问题
n = 100
minimum = float("inf")
point = [(random.randint(0, 3* n), random.randint(0, 3 * n)) for i in range(0, n)]
# 随机生成n个坐标

# print(point)
# print("\n\n\n")
closest_pair = {}
buff = {}
#
# sorted(point, key=lambda p: p[1])
point = sorted(point, key=lambda p: p[0])
print(point)
print(point[1])

plt.xlim(0, 3 * n)
plt.ylim(0, 3 * n)
plt.title("Point Pair")
for i in range(len(point)):
    plt.plot(point[i][0], point[i][1], 'ro-') #画点

def get_distance(a, b):
    # print(a,b)
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)
    if distance in buff:
        buff[distance].append((a, b))
    else:
        buff[distance] = [(a, b)]
    return distance


def judge_minimum(temp):
    global minimum
    global buff
    if temp not in buff:
        return minimum
    if minimum < temp:
        pass
    elif minimum == temp:
        for i in range(0, len(buff[temp])):
            closest_pair[minimum].append(buff[temp][i])
    else:
        minimum = temp
        closest_pair.clear()
        closest_pair[temp] = buff[temp][:]
    return minimum


def min_between(point, left, mid, right, minimum):
    global buff, closest_pair
    for i in range(left, mid):
        if abs(point[i][0] - point[mid][0]) <= minimum:
            for j in range(mid, right):
                if abs(point[i][0] - point[j][0]) <= minimum and abs(point[i][1] - point[j][1]) <= minimum:
                    get_distance(point[i], point[j])
    if len(buff) > 0:
        buff = sorted(buff.items(), key=lambda buff: buff[0])
        temp = buff[0][0]
        buff = dict(buff)
    else:
        temp = float("inf")
    return temp


def divide(point, left, right):
    global minimum, buff
    # right不包括
    if right - left < 2:
        # 如果只有一个点，就没有最小值
        return float('inf')
    elif right - left == 2:
        # 如果有两个点，计算距离并返回
        return get_distance(point[left], point[left + 1])
    else:
        mid = int((left + right) / 2)  # 各点x坐标的中位数

        min_left = divide(point, left, mid) # 分左边，获取左边最小距离
        # print("min_left:",min_left)
        minimum = judge_minimum(min_left)  # 找到目前最小距离并返回

        buff.clear()

        min_right = divide(point, mid, right) # 分右边，获取右边最小距离
        # print("min_right",min_right)
        minimum = judge_minimum(min_right) # 找到目前最小距离并返回
        buff.clear()

        temp = min_between(point, left, mid, right, minimum) # 判断两个区间之间有没有更小的
        # print("temp",temp)
        minimum = judge_minimum(temp)
        buff.clear()

        return min(min_left, min_right, temp)


time_start = time.time()
divide(point, 0, len(point))
time_end = time.time()
print("\n\n\n\nrun_time is :", time_end - time_start)
#
print("\n\n\n" + "The Closest Pair is:",
      closest_pair[minimum], "	Distance:", minimum)
for i in range(0, len(closest_pair[minimum])):
    plt.plot(closest_pair[minimum][i][0][0],
             closest_pair[minimum][i][0][1], "bo-")
    plt.plot(closest_pair[minimum][i][1][0],
             closest_pair[minimum][i][1][1], "bo-")
plt.show()

