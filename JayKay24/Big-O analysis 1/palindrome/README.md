# Analyze the space & time complexity of the following algorithm
## Problem

![Palindrome](./images/Screenshot%202021-10-05%20at%2009.27.14.png)

### Time Complexity

*fn(s) = 1 + 1 + 1 + s/2*

**O(s)** - The condition `if s[i] != s[size - i - 1]` in the for loop will need to be checked as many times as `s / 2`, which translates to **O(s)**.


### Space Complexity

**O(1)** - No auxiliary memory is tied to the size of `s` in the algorithm.

