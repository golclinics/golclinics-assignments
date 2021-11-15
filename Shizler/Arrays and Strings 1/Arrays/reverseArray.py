def reverseArray(A):
    j = len(A)-1
    for i in range(int(len(A)/2)):
        A[i], A[j] = A[j], A[i]
        j -= 1
    print(A)

A = [10,5,1, 6, 9]
reverseArray(A)