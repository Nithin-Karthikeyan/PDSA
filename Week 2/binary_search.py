def binarySearchIndexAndComparisons(L, k):
    # define the indices of left and right
    left, right = 0, len(L)-1
    no_of_compares = 0
    while left <= right:
        no_of_compares += 1
        mid = (left+right)//2
        if k == L[mid]:
            return (True, no_of_compares)
        elif k > L[mid]:
            left = mid+1
        else:
            right = mid-1
    return (False, no_of_compares)



L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]
k = 100
print(binarySearchIndexAndComparisons(L, k))


