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

# Result
# [10, 15, 3, 3, 2, 1]


def rotate_left_optimized(A, d):
    n = len(A)
    x = d % n

    cycle_elements = A[:x]
    # print("Cycle elements: ", cycle_elements)

    for i in range(x, n):
        A[i - x] = A[i]
    # print("Before cycling: ", A)

    temp = 0
    for i in range(n-x, n):
        A[i] = cycle_elements[temp]
        temp += 1

##########################  TESTS  #############################
A = [3, 2, 1, 10, 15, 3]
d = 3   # or d = 9, d = 15, d = 3 + 6n for n = 0, 1, 2, 3, .....
rotate_left_optimized(A, d)
print(A)

# Result
# [10, 15, 3, 3, 2, 1]

A = [3, 2, 1, 10, 15, 3]
d = 1   # or d = 7, d = 13, d = 1 + 6n for n = 0, 1, 2, 3, .....
rotate_left_optimized(A, d)
print(A)

# Result
# [2, 1, 10, 15, 3, 3]

A = [3, 2, 1, 10, 15, 3]
d = 6   # or d = 0, d = 12, d = 6n for n = 0, 1, 2, 3, .....
rotate_left_optimized(A, d)
print(A)

# Result
# [3, 2, 1, 10, 15, 3]

A = [3, 2, 1, 10, 15, 3]
d = 5   # or d = 12, d = 17, d = 5 + 6n for n = 0, 1, 2, 3, .....
A = [3, 2, 1, 10, 15, 3]
rotate_left_optimized(A, d)
print(A)

# Result
# [3, 2, 1, 10, 15, 3]