# Big-O analysis
# Time Complexity: O(n^2)
# Space Complexity: O(n)

# the space complexity is O(N) because the recursive function grows linearly
# relative to the input. e.g:
# f(O) = 0
# f(1) = 0
# f(2) = 1

def countdown_recursive(n):
    if n == 0:  # n operations
        print("Blast off")  # 1 operation
    else:
        print(n)  # 1 operation
        countdown_recursive(n - 1)  # n operations
# 1 + 1 + n * n
# 2 + n**2
