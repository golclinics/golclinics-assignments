# Time Complexity: O(n)
# Space Complexity: O(n)

def is_palindrome(s):
    if len(s) == 0: # s operations
        return True  # an empty string is a palindrome # 1 operation

    size = len(s) # 1 operation
    midpoint = size // 2 # 1 operation

    for i in range(midpoint + 1): # n + 1 operations
        if s[i] != s[size - i - 1]: # 1 operation
            return False # 1 operation
    return True # 1 operation

# s + 1+1+1+s+1+1+1+1
# 2s + 7