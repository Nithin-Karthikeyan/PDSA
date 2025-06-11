def sortInRange(L, r):
    # create a frequency list
    freq_list = [0]*r
    for num in L:
        freq_list[num] += 1
    
    # Iterate thru the list and insert the value corresponding to the index at the freq_list
    idx = 0
    for val in range(r):
        while freq_list[val] > 0:
            L[idx] = val
            idx += 1
            freq_list[val] -= 1
    

