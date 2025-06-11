def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        j=i-1
        while L[j][0] > L[j+1][0] and j>=0:
            L[j], L[j+1] = L[j+1], L[j]
            j -= 1
    print(L)
    return L

def ISort2(L):
    # Assume L is already sorted based on chars
    n = len(L)
    for i in range(1, n):
        j = i-1
        # Sort only if the chars are equal
        if L[j][0] == L[j+1][0]:
            # Compare the digits
            while L[j][1:] > L[j+1][1:] and j>=0:
                L[j], L[j+1] = L[j+1], L[j]
                j -= 1
    print(L)
    return L

def combinationSort(strList):
    L1 = insertionSort(strList)
    L2 = ISort2(L1)
    return L1, L2

    




L = ["d46", "g54", "e69", "d45", "a99"]
L2 = insertionSort(L)
L3 = ISort2(L2)
print(L2, L3)
# print(combinationSort(L))
# print(insertionSort(L))
# print(combinationSort(L))