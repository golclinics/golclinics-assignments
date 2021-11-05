""" def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2
    
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True """

time complexity => O(n)
space complexity => O(1)    