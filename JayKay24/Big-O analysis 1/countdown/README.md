# Analyze the space & time complexity of the following algorithm
## Problem

![Countdown](./images/Screenshot%202021-10-04%20at%2021.47.02.png)

### Time Complexity

*fn(n) = n + n + 1*

**O(n)** - `countdown` will be called as many times as the size of `n`. If `n = 6`, then `print(n)` & `n -= 1` will each be called **6** times.

### Space Complexity

**O(1)** - No auxiliary memory is required to execute the algorithm.