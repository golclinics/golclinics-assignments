# Time complexity: O(n)
# Space complexity: O(n)

def concatenate_arrays(A, B):
    result = [] # 1 operation
    for x in A: # n operations
        result.append(x) # 1 operation
    for y in B: # n operations
        result.append(y) # 1 operation
    return result # 1 operation
# 1 + 2 * n + 2
# 3+2n operations
