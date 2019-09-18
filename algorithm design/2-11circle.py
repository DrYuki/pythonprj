
import numpy as np

def Talbe(k):

    n = 2**k
    a = np.array([[0 for col in range(n)] for row in range(n)])

    a[0,:] = range(1,n+1)
    print(a)
    for s in range(1,k+1):
        step = 2**s
        m = step//2

        for i in range(0,n,step):
            print('step=',step,'i=',i,m)
            # print(i,i + m,i+step)
            # print(a[m:step, i+m:i+step])
            # print(a[0:+ m, i:i + m])
            # print(a[m:step,i:i+m])
            # print( a[0:m, i+m:i+step])
            a[m:step, i+m:i+step] = a[0:m, i:i+m]
            a[m:step,i:i+m] = a[0:m, i+m:i+step]
            print(a)
        print()
    return a
D={
    1: 'RNG',
    2: 'IG',
    3: 'EDG',
    4: 'JDG',
    5: 'LGD',
    6: 'OMG',
    7: 'FPX',
    8: 'SN',
}
a = Talbe(3)

for j in range(2**3):
    print('Day :',j+1)
    for i in range(1,2**3):
        v1 = D[a[i][0]]
        v2 = D[a[i][j]]
        print(v1,' vs ',v2)
