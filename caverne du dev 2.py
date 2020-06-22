def b(L):
    if L[1] > 1:
        L[1] = L[1] - 1
        L[2] = L[2] + 1
        return b(L)
    else:
        return L[2]

M = [3, 2 , 6]
print(b(M))