# Palindrome

Given a string `s` as input, the `is_palindrome(s)` function returns true if `s` is a palindrome
and returns false otherwise. A palindrom in this case is a word that reads the same forward and
backwards, e.g. `madam`

```python
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

## Time Complexity

**O(n)** - The loop in the function runs `n/2 + 1` times, which causes it to have a time complexity of `O(n/2 + 1)`. However, in Big O analysis, constants are ignored, which leads to it being considered as `O(n)`

## Space Complexity

**O(1)** - The variables created in the function are `size` and `midpoint`. However the values of the variables are constant and do not vary directly with the size of the input `n`. Therefore, the space used in the implementation is constant.