This solves the same problem as the previous algorithm, but uses recursion instead of a loop. This might not be obvious if you're not familiar with function call stacks. Bonus points if you can explain why the space complexity here is not the same as the space complexity of the loop-based implementation. Feel free to research on the Internet.
```
def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)

```