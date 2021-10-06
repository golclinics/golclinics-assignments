# Big-O Analysis
# Time complexity: O(2n)
# Space Complexity: O(n^2)

def countdown(n):
    while n > 0: # n times
        print(n) # 1 operation
        n -= 1 # n times
    print("Blast off!") # 1 operation
# n * 1 + n * 1 + 1
# n + n +1
# 2n + 1
# n * n + 2
# O(n)**2
# O(n)
