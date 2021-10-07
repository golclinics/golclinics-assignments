# Countdown recursive

This solves the same problem as the previous algorithm, but uses recursion instead of a loop.
This might not be obvious if you're not familiar with function call stacks. Bonus points
if you can explain why the space complexity here is not the same as the space complexity
of the loop-based implementation. Feel free to research on the Internet.

```python
def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)
```

## Time Complexity

**O(n)** - The `countdown_recursive` function is called as long as the base case(`n == 0`) isn't met. This causes the function to be called for a total of `n` times, as `n` is decreased by 1 on every recursive call, therefore resulting in a linear time complexity

## Space Complexity

**O(n)** - On each recursive call, each instance of the `countdown_recursive` function gets pushed onto the call stack, before being popped out from top to bottom after the base case is satisfied. The total number of recursive calls is `n`, which causes the maximum number of functions in the call stack to equal `n` as well.

## Bonus

The space complexity here is different because in the loop-based implementation, there were no new variables created and the iteration was done in place.
