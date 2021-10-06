# Analyze the space & time complexity of the following algorithm
## Problem

![Countdown recursive](./images/Screenshot%202021-10-04%20at%2022.24.24.png)

### Time Complexity

*fn(n) = fn(n - 1) + fn(n - 2) + ... + fn(0)*

**O(n)** - `countdown_recursive` will be called as many times as the size of `n`. `countdown_recursive(n)` will continue to be
added to the call stack until `n` is **0** (base case). The statement `if n == 0:` is the base case and will return at this point; pending invocations to `countdown_recursive` will be popped off the call stack.

### Space Complexity

**O(n)** - If `n = 6`, there will be as many as **6** frames on the call stack representing pending invocations of `countdown_recursive(n)`. These stack frames require auxiliary memory to be pushed on to the call stack until the base case of `n == 0` is reached, at which point, `print("Blast off")` will be called, and pending frames of `countdown_recursion(n)` will be popped off the call stack.