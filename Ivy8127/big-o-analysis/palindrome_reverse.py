""" def is_palindrome_rev(s):
    reversed_s = s[::-1] 
    return s == reversed_s
print(is_palindrome_rev(s)) """

Time complexity => 0(log(n))
""" def is_palindrome_rev2(s):
    reversed_seq = reversed(s) 
    reversed_s = ''.join(reversed_seq) 
    return s == reversed_s
print(is_palindrome_rev2(s)) """

Time complexity => O(n)
Space complexity => O(n)
