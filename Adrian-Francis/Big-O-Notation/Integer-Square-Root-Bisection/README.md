This solves the same problem as int_sqrt using a different approach: instead of trying out all numbers from 0-x, it tries out the number in the middle of the range, then eliminates half of the range where it's sure the answer cannot be found then keep repeating that process until the answer is found.

```
def int_sqrt_bisect(x):
    low = 0
    high = x
    guess = x // 2
    while True:
        diff = guess * guess - x
        if diff == 0:
            return guess
        if diff < 0: # our guess was lower than the true square root
            low = guess # so we should continue searching in the range [guess - high]
        else: # our diff was higher than the true square root
            high = guess # we continue searching in the range [low - guess]
        
        if high - low <= 1: # at this point we can't an integer square root for x
            break

        guess = (low + high) // 2 # pick a guess in the middle of the new range
    return -1

```