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


# **************  TIME COMPLEXITY  **************
# The time complexity is O(n)


# **************  SPACE COMPLEXITY  **************
# The space complexity is O(n)