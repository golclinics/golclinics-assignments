# Analyze the space & time complexity of the following algorithm
## Problem

```python
def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s

def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s
```

### Time Complexity

1. `is_palindrome_rev(s)` - **O(s)** - `s[::-1]` returns a copy of the reversed `s`. This reversal operation potentially "touches" each character of `s` and thus the operations involved in the reversal are dependent on the size of `s`.
2. `is_palindrome_rev2(s)` - **O(s)** - `reversed_s = ''.join(reversed_seq)` builds a new reversed string from the iterator `reversed_seq` and assigns it to the variable `reversed_s`. Building up this new reversed string is dependent on the size of `s`.

### Space Complexity

 **O(s)** - Both methods store the built reversed string in variable `reversed_s`, to be used later for comparison.
