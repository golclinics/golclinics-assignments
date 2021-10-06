# Time complexity: O(n)
# Space complexity: O(1)

def int_sqrt(x):
    for i in range(x): # n operations
        if i * i == x: # 1 operation
            return i # 1 operation

    return -1 # 1 operation

# n + 3
