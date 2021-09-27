import timeit

def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2

    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True


def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s


def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s


def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True

    # in python s[-1] is the last element of the sequence s, i.e. "madam"[-1] -> "m"
    # and s[1: -1] will create a slice starting from the second element to the second last element
    # "madam"[1: -1] -> "ada"
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])


s = "m" * 500 + "u" + "m" * 500 # this creates a string with 1001 characters, 500 'm' followed by a 'u' followed by 500 'm'.

# This will execute is_palindrome(s) 1000 times and return the average execution time in seconds
result = timeit.timeit(lambda: is_palindrome(s), number=1000)
print("is_palindrome time:", result)
result = timeit.timeit(lambda: is_palindrome_rev(s), number=1000)
print("is_palindrome_rev time:", result)
result = timeit.timeit(lambda: is_palindrome_rev2(s), number=1000)
print("is_palindrome_rev2 time:", result)
result = timeit.timeit(lambda: is_palindrome_recur(s), number=1000)
print("is_palindrome_recur time:", result)


# Results
# is_palindrome time: 0.07176800700017338       (Third)
# is_palindrome_rev time: 0.0014009719998284709 (Fastest)
# is_palindrome_rev2 time: 0.030794706999586197 (Second)
# is_palindrome_recur time: 0.1671632799998406  (Slowest)