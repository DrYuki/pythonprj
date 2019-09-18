import random


def partition(a, p, r):
    x = a[p]
    low = [m for m in a[p:r] if m <x ]
    high = [m for m in a[p:r] if m >= x]
    a[p:r] = low + high
    return len(low)

def partition2(a, p, r,x):
    # 考虑到x有很多的情况，需要带等号！
  #  print(a[p:r])
    low = [m for m in a[p:r+1] if m < x]
    high = [m for m in a[p:r+1] if m >= x]
    a[p:r+1] = low + high
    return len(low)


def Select(a, p, r, k):
    if p == r:
        return a[p]
    i = partition(a, p, r)
    j = i - p + 1
    if k <= j:
        return Select(a, p, i, k)
    else:
        return Select(a, i+1, r, k-j)

# 线性方法
def SelectLine(a,p,r,k):
    if r-p < 75:
        a[p:r+1] = sorted(a[p:r+1])
        return a[p+k-1]
    n = (r-p-4)//5
    i = 0

    while i < n:
        n1 = p + 5*i
        list1 = sorted(a[n1:n1+5])
        print(a)
        print(n1+1,p+i)
        a[n1+2] = a[p+i]
        i +=1
        a[p+i] = list1[2]

    x = SelectLine(a, p, p+n, (r-p-4)//10)
    print('x:',x)
  #  b =a.copy()
  #  b.sort()
    i = partition2(a, p, r+1, x)

  #  print('index: ', b.index(x),i)
  #  print('!!!i =',i, p, r, x)

    j = i-p+1
    m = len([item for item in a[p:r+1] if item == x])
    if m > 1 and j <= k <= j+m-1:
        print('herhe!!!')
        return a[i]
    if k<=j :
        return SelectLine(a,p,i,k)
    else:
        return  SelectLine(a,i+1,r, k-j)



#a = [random.randint(1,1000) for i in range(100)]
# a = [14, 2, 34, 43, 21, 19]
a = [1]*1000
print(a)
# print(quick_sort(a))
q = 2
k = 2
# print(Select(a,0,len(a)-1,2))
print(SelectLine(a,0,len(a)-1, k))
# 太大就爆栈了！！！
a.sort()
#print(a)
print(a[k-1])
# print(a)