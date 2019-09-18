import random
import numpy
import math
import time
import matplotlib.pyplot as plt

n = 512*512
minimum = float("inf")
point = [(random.randint(0, 3* n), random.randint(0, 3 * n)) for i in range(0, n)]
# 随机生成n个坐标

# print(point)
# print("\n\n\n")
# closest_pair = {}
# buff = {}

# point2 = sorted(point, key=lambda p: p[0])
#
# plt.xlim(0, 3 * n+5)
# plt.ylim(0, 3 * n+5)
# plt.title("Point Pair")
# for i in range(len(point2)):
#     plt.plot(point2[i][0], point2[i][1], 'ro-') #画点


def Distantce(a,b):
    return a,b,math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def DisAngle(p1,p2,p3):
    a,b,d1 = Distantce(p1,p2)
    a,b,d2 = Distantce(p2,p3)
    a,b,d3 = Distantce(p3,p1)
    D = {d1:[p1,p2],d2:[p2,p3],d3:[p3,p1]}
    d = min(d1,d2,d3)
    [a,b] = D[d]
    return a,b,d

def Cpair2(p,d):
    # px 按X排序点集，py按y排序点集
    if len(p) ==1:
        return None
    if len(p) == 2:
       return Distantce(p[0], p[1])
    if len(p) == 3:
       return DisAngle(p[0], p[1],p[2])
    d1 = float("inf")
    d2 = float("inf")
    d3 = float("inf")
    # 多于3个点的情况
    temp = sorted(p,key=lambda item: item[0])
    m = temp[len(temp)//2][0]
    # print('temp=',temp)
    # print('m=',m)
    # 按照 m 分割
    s1 = temp[0:len(temp)//2]
    s2 = temp[len(temp)//2:]
    # print('s1=',s1)
    # print('s2=', s2)

    [a1,b1,d1] = Cpair2(s1,d1)
    [a2,b2,d2] = Cpair2(s2,d2)
    # print(d1, d2)
    dm = min(d1,d2)


    if d1 == dm:
        a, b = a1,b1
    else:
        a, b,=a2, b2

    # p1,p2是距离垂直分割线l 距离在dm之内所有点的集合
    p1 = [item for item in s1 if m-item[0] <= dm]
    p2 = [item for item in s2 if item[0]-m <dm]

    # 按照Y坐标大小排序
#    p1 = sorted(p1, key=lambda item: p[1])
#    p2 = sorted(p2, key=lambda item: p[1])

    # 合并
    for px in p1:
        for py in p2:
            if abs(py[1]-px[1])<dm :
                a3, b3, d3 = Distantce(px,py)
                if(d3 < dm):
                    dm = d3
                    a, b = a3, b3

    d = min(d1,dm)


    return a, b, d




time_start = time.time()
[a, b, d] =Cpair2(point, float("inf"))
time_end = time.time()
print(a)
print(b)
print(d)
print("\n\n\n\nrun_time is :", time_end - time_start)
#
# plt.plot(a[0],a[1], "bo-")
# plt.plot(b[0],b[1], "bo-")
# plt.show()