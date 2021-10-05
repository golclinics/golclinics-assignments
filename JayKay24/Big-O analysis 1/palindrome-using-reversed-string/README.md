# Analyze the space & time complexity of the following algorithm
## Problem

![Palindrome using reversed string](./images/Screenshot%202021-10-05%20at%2009.57.38.png)

### Time Complexity

1. `is_palindrome_rev(s)` - **O(s)** - `s[::-1]` returns a copy of the reversed `s`. This reversal operation potentially "touches" each character of `s` and thus the operations involved in the reversal are dependent on the size of `s`.
2. `is_palindrome_rev2(s)` - **O(s)** - `reversed_s = ''.join(reversed_seq)` builds a new reversed string from the iterator `reversed_seq` and assigns it to the variable `reversed_s`. Building up this new reversed string is dependent on the size of `s`.

### Space Complexity

 **O(s)** - Both methods store the built reversed string in variable `reversed_s`, to be used later for comparison.
