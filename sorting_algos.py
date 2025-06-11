def selectionSort(L):
    """ 
    Iterate through each element of the list, compare it with every other element, and swap the two if lower value is found.
    Repeatedly select the minimum from the unsorted part and swap it to the front.
    """
    n = len(L)
    for i in range(n-1):
        for j in range(i, n):
            if L[j] < L[i]:
                L[i], L[j] = L[j], L[i]
    return None

def insertionSort(L):
    """ 
    Iterate through each element, if the previous element is smaller than the current, then swap the two.
    Build a sorted section one element at a time by inserting each new element into its proper place.
    """
    n = len(L)
    for i in range(1, n):
        j = i-1
        while L[j] > L[j+1] and j>=0:
            L[j+1], L[j] = L[j], L[j+1]
            j -= 1
    return None

def mergeSort(L):
    # Define the merge function to merge both the sorted lists
    def merge(L, R):
        # Iterate over both the lists until one of them runs out of elements
        ret = []
        i, j = 0, 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                ret.append(L[i])
                i += 1
            else:
                ret.append(R[j])
                j += 1

        ret.extend(R[j:])
        ret.extend(L[i:])
        return ret
    
    if len(L) <= 1:
        return L
    
    mid = len(L)//2
    left = mergeSort(L[:mid])
    right = mergeSort(L[mid:])
    return merge(left, right)

        


L1 = [7,6,5,4,3,2,1,1,1]
L2 = [7,6,5,4,3,4,1,1,1]
L3 = [3,164,1274,61,384,27,39,17,20,20,-1,27,39,12]
L4 = [2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2]
insertionSort(L2)
selectionSort(L1)
print(L1)
print(L2)
print(mergeSort(L4))