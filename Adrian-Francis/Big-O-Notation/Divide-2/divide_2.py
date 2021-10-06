# Time complexity: O(n^2)
# Space Complexity: O(n)

def count_div_2(n):
    count = 0 # 1 operation
    while n > 1: # n operations
        n = n // 2 # n/2 operations
        count += 1 # 1 operation
    return count # 1 operation

# 1 + n * n/2 + 2
# n^2/2 + 3
