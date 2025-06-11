def mergeInPlace(L1, L2):
    l1, l2 = len(L1), len(L2)
    L1.extend(L2)
    L1.sort()
    return L1[:l1], L1[l1:l1+l2]

L1 = [4,6]
L2 = [1,3,6,10]
print(mergeInPlace(L1, L2))


