# Analyze the space & time complexity of the following algorithm
## Problem

![Palindrome using recursion](./images/Screenshot%202021-10-05%20at%2009.27.14.png)

### Time Complexity

*fn(s) = fn(s - 2) + fn(s - 4) + ... + fn(0)*

**O(s)** - `is_palindrome_recur(s[1:-1])` will be called recursively as many times as *s/2*. Removing the *1/2* constant, this
translates to **O(s)**.


### Space Complexity

**O(s)** - There will be as many as *s/2* frames on the call stack before either base case is hit.
