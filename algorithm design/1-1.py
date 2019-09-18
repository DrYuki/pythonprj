import os
import evaluate
def counteach(n,i):
    pos = 1   # 位置
    icount = 0   # 计数, 自己先算一个
    low = 0  # 低位数字
    high =0  # 高位数字
    currn=0  #当前位数字

    while n//pos!=0:
        currn = n//pos % 10
        low = n - n//pos*pos
        high = n//(pos*10)

        if currn < i:
            icount += high *pos
        elif currn == i:
            icount += high*pos + low +1
        elif currn > i:
            icount += (high+1)*pos

        if i == 0:
            icount -= pos

        pos *= 10
    return icount


def count(n):
    res = [0] * 10
    for i in range(0, 10):
        res[i] += counteach(n,i)
    return res


path =r'.\source\prog11\test'
path2 =r'.\source\prog11\answer'
iii = 0
for filename in os.listdir(path):
    print(filename)
    name = "%s\\%s"%(path,filename)
    for line in open(name):
        res = count(int(line))
      #  print(res)
    name2 = "%s\\myout%d.out" % (path2, iii)
    fout = open(name2, 'w')
    for line in res:
        fout.write(str(line) + '\n')
    fout.close()
    # 评估

    name3 = "%s\\count%d.out" % (path2, iii)
    evaluate.ev(name3, name2)
    iii += 1







