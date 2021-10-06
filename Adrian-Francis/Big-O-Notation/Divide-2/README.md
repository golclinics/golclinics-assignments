The count_div_2(n) functions counts the number of times the input number n can be divided by 2 before it reaches one or less.

The time complexity may not be immediately obvious to all, but here's a hint: Count the number of iterations that this functions makes when then input is 4, 5, 6, 7, 8. At which values of n does the number of iterations increase compared to when n = 4? Now keep trying for values > 8, at which point does the number of iterations increase by 1 compared to when n=8? Do you see a pattern or trend between the growth in n and how that affects the increase in iterations? In general, how much should n grow before count increases by 1? Do you see a mathematical releationship n and the total number of iterations?
```
def count_div_2(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count

```