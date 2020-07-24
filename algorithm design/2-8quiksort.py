import random


# 书上的算法
def quicksort(L, p, r):
    print("start")
    showList2(L, -1, -1, p)
    if p < r:
        q = partion(L, p, r)
        print('left')
        quicksort(L, p, q)
        print('right')
        quicksort(L, q+1, r)
    else:
        print('nothing')
    return L


def showList(L,j):
    for item in L[0:j]:
        print(item, end=' ')
    print(" [", L[j], "] ", end=' ')
    for item in L[j+1:]:
        print(item, end=' ')
    print()

def showList2(L,i,j,k):
    for idx in range(len(L)):
        if idx == i or idx == j:
            print('(%3d)' % L[idx],end=" ")
        elif idx == k:
            print('[%3d]' % L[idx],end=" ")
        else:
            print(' %3d ' % L[idx],end=" ")
    print()

    if i == k:
        D = {i: ' i/p ', j: '  j  '}
    elif j ==k :
        D = {i: '  i  ', j: ' j/p '}
    else:
        D = {i: '  i  ', j: '  j  ', k: '  p  '}
    for idx in range(len(L)):
         if idx in  D.keys():
             print( D[idx] ,end=' ')
         else:
             print("     ", end=' ')
    print()

    return


def partion(L,p,r,israndom = True):

    if israndom:
        temp = random.randint(p,r-1)
        L[temp],L[p] = L[p],L[temp]
    print("random")
    showList2(L, -1, -1, p)
    x = L[p]
    i = p
    j = r+1
    # 将小于x的元素交换到左边区域，将大于x的元素交换到右边区域
    while True:
        for item in range(p,r): # 找第一个大于x的下标
            i += 1
            if L[i] >= x:
                break
        for item in range(r+1,0,-1): # 找第一个小于x的下标
            j -= 1
            if L[j] <= x:
                break
        showList2(L, i, j, p)
        if i >= j:
            print('break!')  # 此时 p 在i j 中间，j<p<i --> swap(p,j)
            break
        print('change! swap(i,j)') # 此时 p 在 i,j 的左侧 p < i < j  -->swap(i,j)
        L[i], L[j] = L[j], L[i]
        showList2(L, i, j, p)

    print("out swap(p,j)")

    L[p] = L[j]
    L[j] = x
    showList2(L, i, p, j)
    print()
    return j


#直观算法
def quick_sort(L):
    """快速排序"""
    b = L.copy() # 防止修改
    if len(b) < 2:
        return b
    # 选取基准，随便选哪个都可以，选中间的便于理解
    mid = b[len(b) // 2]

    # 定义基准值左右两个数列
    left, right = [], []
    # 从原始数组中移除基准值
    b.remove(mid)
    for item in b:
        # 大于基准值放右边
        if item >= mid:
            right.append(item)
        else:
            # 小于基准值放左边
            left.append(item)
    # 使用迭代进行比较
    return quick_sort(left) + [mid] + quick_sort(right)

def partition(a,p,r,x):
    low = [m for m in a if m < x]
    high = [m for m in a if m > x]
    a[p:r] = low + [x] + high
    return len(low)

a = [random.randint(1,100) for i in range(60)]
#a = [14, 2, 34, 43, 21, 19]

for i in a:
    print(i, end=' ')
print("\n")
#print(quick_sort(a))
# q = random.randint(0, len(a)-2)
q =2
# print(quicksort(a, 0, len(a)-1))
a.sort()
for i in a:
    print(i, end=' ')