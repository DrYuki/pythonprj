import os
import evaluate


def f(i ,k):
    #以 i开头，k位数有多少个
    c = 0
    if k ==1:
        c = 1
    elif k==0:
        c = 0
    else:
        for j in range(i+1,26):
            c +=f(j,k-1)
    return c


def g(k):
    c = 0
    if k ==1:
        c = 1
    elif k==0:
        c=0
    else:
        for i in range(1,26):
            for j in range(i+1,26):
                c += f(j,k-1)
    return c


def isas(str):
    # 判断升序:
    if(len(str)>2):
        for j in range(0, len(str) - 1):
            print(j)
            if str[j] >= str[j + 1]:
                print(str[j] + '!!!' + '!!!' + str[j + 1])
                return False
    return True


def encode(str):
    code = 0
    str = list(str)
    str = str[:-1]
    print(str)
    if(isas(str)):
#     判断是否符合升序
        code += g(len(str)-1) # 比其短的位数
        #同样的位数
        for i in range(0, ord(str[0])-ord('a')-1):
            code += f(i, len(str))
        #首字母开头相同
        code += f(ord(str[0])-ord('a'), len(str))
    else:
        code = 0
    return code

#print(isas('a\n'))
code = encode('ab\n')
print(code)

# 读文件
# path =r'.\source\prog12\test'
# path2 =r'.\source\prog12\answer'
#
# # 计算
# iii = 0
# for filename in os.listdir(path):
#     print(filename)
#     name = "%s\\%s"% (path, filename)
#     for line in open(name):
#         iii +=1
#         name2 = "%s\\myout.out" % (path2)
#         fout = open(name2, 'w')
#         if iii > 1:
#             code = encode(line)
#             print("$$$$$$$$")
#             print(code)
#             fout.write(str(code)+'\n')
#         fout.close()
#
# # 测试
# name1 = "%s\\encode.out" % (path2)
# name2 = "%s\\myout.out" % (path2)
# evaluate.ev(name1,name2)


