# Countdown

Given an integer `n` as input `countdown(n)` prints the numbers n to 1 in descending
order then prints "Blast off!"

```python
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
```

## Time Complexity

**O(n)** - The loop in the `countdown` function runs as long as `n` is greater than 0. On each iteration, `n` is decreased by 1, which causes the loop to run for a total of `n` times, i.e linear time.

## Space Complexity

**O(1)** - No new variables were created in the function, therefore it uses constant space.
