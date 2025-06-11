def find_Min_Difference(L, P):
    # Establish the min diff
    min_diff = pow(10, 11)
    # Sort the list
    L.sort()
    # make subset using sliding window
    superset = []
    for i in range(0, len(L)-P+1):
        superset.append(L[i:i+P])
    print(superset)
    # Find the min diff from these subsets
    for subset in superset:
        diff = subset[4] - subset[0]
        if  diff < min_diff:
            min_diff = diff
    print(min_diff)
    return min_diff
        

L=eval(input().strip())
P=int(input())
print(find_Min_Difference(L,P))

    
