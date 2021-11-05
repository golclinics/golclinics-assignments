""" def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])
print(is_palindrome_recur(s)) """

Time complexity => O(n**2)
Space complexity => O(n)