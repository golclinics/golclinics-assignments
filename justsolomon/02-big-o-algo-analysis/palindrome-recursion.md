# Palindrome using recursion

This implementation is similar to the loop-based version in that it compares a pair of letters
at equal distances from the middle of the string in each iteration. But it does so using
recursion instead of a loop:

```python
def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    
    # in python s[-1] is the last element of the sequence s, i.e. "madam"[-1] -> "m"
    # and s[1: -1] will create a slice starting from the second element to the second last element
    # "madam"[1: -1] -> "ada"
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])
```

## Time Complexity