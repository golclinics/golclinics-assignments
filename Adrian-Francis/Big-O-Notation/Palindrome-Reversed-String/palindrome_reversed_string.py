# Time complexity: O(n)
# Space Complexity: O(n)

def is_palindrome_rev(s):
    reversed_s = s[::-1]  # This is a neat trick to reverse a string in python
    # 1 operation
    return s == reversed_s # s operations


# Time Complexity: O(n)
# Space Complexity: O(n)

def is_palindrome_rev2(s):
    reversed_seq = reversed(
        s)  # creates a sequence with the characters in the string in reverse
    # 1 operation
    reversed_s = ''.join(
        reversed_seq)  # transformed the reversed sequence into a string
    # 1 operation
    return s == reversed_s # s operations

# 1 + 1 + n
