# Time complexity: O(n^2)
# Space Complexity: O(n)
def is_palindrome_recur(s):
    if len(s) == 0: # n operation
        return True # 1 operation
    if len(s) == 1: # n operation
        return True # 1 operation

    # in python s[-1] is the last element of the sequence s, i.e. "madam"[-1] -> "m"
    # and s[1: -1] will create a slice starting from the second element to the second last element
    # "madam"[1: -1] -> "ada"

    return s[0] == s[-1] and is_palindrome_recur(s[1:-1]) # 1 operation
# n+1*n+1+1
# n^2+n+n+1+1
# n^2+ 2n+ 2

# is_palindrome_rev is more efficient since it has linear time and space complexities
# I'd prefer is_palindrome_rev since it very simple and efficient