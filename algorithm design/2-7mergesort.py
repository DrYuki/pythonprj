import random


# 合并两个List
def Merge(a,b):
    global times
    times +=1
    c = []
    h = j =0
    while j <len(a) and h <len(b):
        if a[j] <= b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    # 看哪个数组还剩的
    if j==len(a):
        c = c + b[h:]
    else:
        c = c + a[j:]
    print(c)
    return c


# 合并排序，递归版
def Mergesort_rec(L,ascend = True):

    if len(L) <= 1:
        return L
    mid = len(L)//2
    left = Mergesort(L[:mid],ascend)
    right = Mergesort(L[mid:], ascend)
    print( left, ',', right,end='-->')
    return Merge(left, right)

# 非递归版
def Mergesort(L,ascend = True):
    s = 1
    while s < len(L):
        step = s+s
        for i in range(0, len(L), step):
            left = L[i:i+s]
            right = L[i+s:i+step]
           # print(s, i, i+s, i+step)
            print(left, ',', right, end='-->')
            L[i:i+step] = Merge(left,right)
        s +=s
    return L

# a = [14, 2, 34, 43, 21, 19]
a = [random.randint(1,100) for i in range(10)]
print(a)

b = a
times = 0
print('Mergesort:\n ', Mergesort(a), times)
times = 0
print('Mergesort_rec:\n ',Mergesort_rec(a),times)
b.sort()
print(b)

