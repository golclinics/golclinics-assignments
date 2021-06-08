Given a string s as input, the is_palindrome(s) function returns true if s is a palindrome and returns false otherwise. A palindrom in this case is a word that reads the same forward and backwards, e.g. madam
```
def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2
    
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True

```