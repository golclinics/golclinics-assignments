def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item

# **************  TIME COMPLEXITY  **************
# The time complexity is O(n2)


# **************  SPACE COMPLEXITY  **************
# The space complexity is O(n2)