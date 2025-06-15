# ls = [1,2,3,3,134,234,1]
# print([1,2,3,3,134,234,1].sort())
# ls.sort()
# l = [(1)]
# s = 10.5
# S = 'SAdlh'
# print(S[:4])
# item = int(s)
# print(ls)

# def f(n):
#     s = 0
#     for i in range(2,n):
#         if n%i==0 and i%2==1:
#             s +=1 
#     return s
# niga = "Helo"
# print("Hello, ", niga)
# print(f(59))

# try:
#     print(ls[5])
#     print(ls[10])
# except:
#     print("ERROR")

# print(5//2)

# print("b87" < "c65")
# print("44" < "45")

# def ssort(L):
#     min = pow(-10, 11)
#     n = len(L)
#     for i in range(n-1):
#         for j in range(i, n):
#             if L[j] < L[i]:
#                 L[i], L[j] = L[j], L[i]
#     return L

# print(ssort(ls))

def selectionsort_with_counter(L):
    n = len(L)
    if n < 1:
        return L, 0
    
    effective_swaps = 0
    
    for i in range(n-1):
        minpos = i
        for j in range(i+1, n):
            if L[j] < L[minpos]:
                minpos = j
        
        # Only count as effective swap if minpos != i
        if minpos != i:
            L[i], L[minpos] = L[minpos], L[i]  # Swap operation
            effective_swaps += 1
    
    return L, effective_swaps

# Test on the given list
L = [5, 2, 8, 2, 4]
sorted_list, swaps = selectionsort_with_counter(L.copy())
print(f"Sorted list: {sorted_list}")
print(f"Effective swaps: {swaps}")

print("changes has been made")
