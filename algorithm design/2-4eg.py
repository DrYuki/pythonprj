
def perm(L, k, m, count=0): #产生L[k:m]的所有排列
    count += 1
    #print(count)
    if k == m:
        print(L[0:m+1])
        L[-1] += 1
    else:
        for i in range(k, m+1):
            L[k], L[i] = L[i], L[k]# Ri=R-{ri}
            perm(L, k+1, m, count)# _ perm(Ri) _
            L[k], L[i] = L[i], L[k] # (Ri)perm(Ri)
    return count

max =5
L = [n for n in range(max)]
L= L+[0]
print(L)
perm(L, 0, max-1)
print(L[-1])

