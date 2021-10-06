# Analyze the space & time complexity of the following algorithm
## Problem

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

### Time Complexity

*fn(s) = fn(s - 2) + fn(s - 4) + ... + fn(0)*

**O(s)** - `is_palindrome_recur(s[1:-1])` will be called recursively as many times as *s/2* before either base case is hit. If `s = 'racecar'`, `is_palindrome_recur(s[1:-1])` will be called roughly *7/2* times, which is *4*. Removing the *1/2* constant, this translates to **O(s)**.

### Space Complexity

**O(s)** - There will be as many as *s/2* frames on the call stack before either base case is hit.
