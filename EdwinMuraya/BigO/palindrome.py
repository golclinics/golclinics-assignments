# the function is depend on the lenght of s
# We loop once to the midpoint making it O(1/2 s)
# With increase in the length of the string s >
# the number of the loops increases propotionaly.

## Since big o we are intrested with the worst case scenario. # we usuall drop the constants

# the time complexity of the function  therefore O(n) Linear


def is_palindrome(s):
    if len(s) == 0:
        return True
    size = len(s)
    midpoint = size // 2

    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True


asn = is_palindrome("maam")
print(asn)
