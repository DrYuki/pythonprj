
def q(n,m):

    if n<1 or m<1:
        print('step 1 : q(%d,%d)' % (n, m))
        return 0
    if n==1 or m==1:
        print('step 2 : q(%d,%d)' % (n, m))
        return 1
    if n < m:
        print('step 3: q(%d,%d)'%(n,m))
        return q(n,n)
    if n == m:
        print('step 4 : q(%d,%d)' % (n, m))
        return  q(n, m-1) + 1
    if n > m :
        print('step 5 : q(%d,%d)' % (n, m))
        return  q(n,m-1) + q(n-m,m)


def spadd(n):
    stack = []
    return q(n,n)


def showsp(sum,k,prio,L):
    # 深度优先搜索
    # L 第一位表示和
    if sum > L[0]:
        return
    if sum == L[0]:
        c = []
        for i in L:
            if i > 0:
               c.append(i)
        c = [str(i) for i in c]
        print(c[0]+'='+'+'.join(c[1::]))

        ...
    else:
        for j in range(prio, 0, -1):
            L[k] = j
            sum += j
          #  print('showsp(%d, %d, %d ,L)'%(sum, k+1, j))
            showsp(sum, k+1, j ,L)
            sum -=j



c = spadd(6)
print('totoal is %d' % (c))
L = [0]*7
L[0]=6
showsp(0,1,6,L)