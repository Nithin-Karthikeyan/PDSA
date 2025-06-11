def mergeInPlace(A, B):
    a, b = len(A), len(B)
    for i in range(a):
        for j in range(b):
            if B[j] < A[i]:
                A[i], B[j] = B[j], A[i]
    
    # Sort B
    for i in range(b):
        for j in range(i+1, b):
            if B[j] < B[i]:
                B[j], B[i] = B[i], B[j]
    print(A, B)

A = [2,4,6,9,13,15]
B = [1,3,5,10]
mergeInPlace(A, B)
print(type(A))
