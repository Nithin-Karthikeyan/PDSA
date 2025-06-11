def findLargest(L):
    # The list is shifted to the right n times
    # [1,2,3,4,5] -> [5,1,2,3,4] -> [4,5,1,2,3] -> [3,4,5,1,2] -> [2,3,4,5,1] -> [1,2,3,4,5]
    
    if not L:
        return None
    n = len(L)
    if n == 1:
        return L[0] 
    
    l, r = 0, n-1
    if L[l] < L[r]:
        return L[r]
    
    while l <= r:
        mid = (l+r)//2
        if mid < n-1 and L[mid] > L[mid+1]:
            return L[mid]
        if mid > 0 and L[mid] < L[mid-1]:
            return  L[mid-1]
        if L[mid] > L[l]:
            l = mid+1
        else:
            r = mid-1
    return L[n-1]


L = [1,2,3,4,5]
L2 = [3,4,5,1,2,69]
print(findLargest(L))
print(findLargest(L2))
