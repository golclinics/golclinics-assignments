# Analyze the space & time complexity of the following algorithm
## Problem

```python
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
```

### Time Complexity

*fn(n) = n + n + 1*

**O(n)** - `print(n)` & `n -= 1` will be called as many times as the size of `n` as long as `n > 0` in the loop. If `n = 6`, then `print(n)` & `n -= 1` will each be called **6** times.

### Space Complexity

**O(1)** - No auxiliary memory is tied to the size of `n` in the algorithm.