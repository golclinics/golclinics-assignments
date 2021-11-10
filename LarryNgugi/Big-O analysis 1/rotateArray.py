def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)-1):
            A[i] = A[i + 1]
        A[-1] = first_item


A = [3, 2, 1, 10, 15, 3]
d = 3
rotate_left(A, d)
print(A)


def rotate_left_optimized(A, d):
    n = len(A)
    x = d % n

    cycle_elements = A[:x]

    for i in range(x, n):
        A[i - x] = A[i]

    temp = 0
    for i in range(n-x, n):
        A[i] = cycle_elements[temp]
        temp += 1

A = [3, 2, 1, 10, 15, 3]
d = 3   
rotate_left_optimized(A, d)
print(A)



A = [3, 2, 1, 10, 15, 3]
d = 1   
rotate_left_optimized(A, d)
print(A)


A = [3, 2, 1, 10, 15, 3]
d = 6   
rotate_left_optimized(A, d)
print(A)



A = [3, 2, 1, 10, 15, 3]
d = 5  
A = [3, 2, 1, 10, 15, 3]
rotate_left_optimized(A, d)
print(A)

