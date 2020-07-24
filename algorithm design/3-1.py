import numpy as np

#求最优值 并记录相关信息
def MatrixChain(p,n,m,s):
    #单个矩阵连乘的次数
    print(s)
    for i in range(n):
        m[i][i]=0

    #R 表示连乘的个数 从2开始 2 3 4 5
    for r in range(2,n+1):
        #从第i个矩阵Ai开始，长度为r,循环次数为n-r+1
        for i in range(n-r+1):
            j=i+r-1#当前矩阵端（Ai-Aj）起始为Ai 结尾为Aj
            # print(i,j)
            #第一个重复 m[i][j]=m[i][i]+m[i+1][j]+p[i]p[i+1]p[j+1] i的行列*j的列
            m[i][j]=m[i+1][j]+p[i]*p[i+1]*p[j+1]
            s[i][j]=i
            for k in range(i+1,j):
                # p[i]p[k+1]p[j+1] i的行*k的列*j的列
                t=m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1]
                if t<m[i][j]:
                    m[i][j]=t
                    s[i][j]=k


# 备忘录方法
def LookupChain(p,i,j,s):
    if m[i][j]>0 :
        return m[i][j]
    if i == j:
        return 0
    u = LookupChain(p, i, i, s) + LookupChain(p,i+1, j,s) + p[i]*p[i+1]*p[j+1]
    s[i][j] = i
    for k in range(i+1,j):
        t = LookupChain(p, i, k, s) + LookupChain(p,k+1, j,s) + p[i]*p[k+1]*p[j+1]
        if t < u:
            u = t
            s[i][j]=k
    m[i][j]=u
    return u



def MemoizeMatrixChain(p,n,m,s):
    for i in range(n):
        for j in range(i,n):
            m[i][j] = 0
        return LookupChain(p,0,n-1,s)



def Traceback(i,j,res,s):
    if i==j:
        res.append('A'+str(i))
    else:
        res.append('(')
        Traceback(i, int(s[i][j]),res, s)
        Traceback(int(s[i][j] + 1), j,res, s)
        # print(i,int(s[i][j]),int(s[i][j]+1),j)
        res.append(')')


# arr=[[3,2],[2,5],[5,10],[10,2],[2,3]]
arr=[[30,35],[35,15],[15,5],[5,10],[10,20],[20,25]]


n=len(arr)
# 处理矩阵的行和列
p=[]
for i in range(n):
   if i==0:
       p.append(arr[0][0])
       p.append(arr[0][1])
   else:
       p.append(arr[i][1])
print(p)

# 存储最优值
m=np.zeros((n,n))
#存储最优决策
s=np.full([n,n],-1)
# MatrixChain(p,n,m,s)
#记录最优决策并构造最优解


MemoizeMatrixChain(p,n,m,s)
print(m)
print(s)

res=[]
Traceback(0,n-1,res,s)
print(''.join(res))

m=np.zeros((n,n))
s=np.full([n,n],-1)
MatrixChain(p,n,m,s)
print(m)
print(s)
res=[]
Traceback(0,n-2,res,s)
print(''.join(res))
