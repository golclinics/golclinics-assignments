# Time Complexity: O(n^2)
# Space Complexity: O(1)

def rotate_left(A, d):
    for _ in range(d): # n operations
        first_item = A[0] # 1 operation
        for i in range(len(A)): # n operations
            A[i] = A[i + 1] # 1 operation
        A[-1] = first_item # 1 operation

# n+1 * n +2
# n^2 + 3

