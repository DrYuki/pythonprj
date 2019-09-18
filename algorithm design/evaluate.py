
def ev(filename1, filename2):
    #两个文件逐行比较大小
    std = open(filename1)
    eva = open(filename2)

    error = 0
    i =1
    for line1 in std.readlines():
        line2 = eva.readline()
        if line1 != line2:
            print('error %d line %d: %s %s   ', error, i , line1, line2)
            error +=1
        i += 1
    if error == 0:
        print("correct!")
