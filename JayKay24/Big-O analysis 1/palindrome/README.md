# Analyze the space & time complexity of the following algorithm
## Problem

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

### Time Complexity

*fn(s) = 1 + 1 + 1 + s/2*

**O(s)** - The condition `if s[i] != s[size - i - 1]` in the for loop will need to be checked as many times as `s / 2`, which translates to **O(s)**.


### Space Complexity

**O(1)** - No auxiliary memory is tied to the size of `s` in the algorithm.

