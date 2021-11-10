import timeit

def is_palindrome(s):
    if len(s) == 0:
        return True   

    size = len(s)
    midpoint = size // 2

    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True


def is_palindrome_rev(s):
    reversed_s = s[::-1] 
    return s == reversed_s


def is_palindrome_rev2(s):
    reversed_seq = reversed(s) 
    reversed_s = ''.join(reversed_seq) 
    return s == reversed_s


def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True

   
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])


s = "m" * 500 + "u" + "m" * 500 

result = timeit.timeit(lambda: is_palindrome(s), number=1000)
print("is_palindrome time:", result)
result = timeit.timeit(lambda: is_palindrome_rev(s), number=1000)
print("is_palindrome_rev time:", result)
result = timeit.timeit(lambda: is_palindrome_rev2(s), number=1000)
print("is_palindrome_rev2 time:", result)
result = timeit.timeit(lambda: is_palindrome_recur(s), number=1000)
print("is_palindrome_recur time:", result)


