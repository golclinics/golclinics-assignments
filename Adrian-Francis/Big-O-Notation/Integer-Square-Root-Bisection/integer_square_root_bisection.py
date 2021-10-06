# Time complexity: O(n)
# Space complexity: O(n)

def int_sqrt_bisect(x):
    low = 0 # 1 operation
    high = x # 1 operation
    guess = x // 2 # 1 operation
    while True: # 1 operation
        diff = guess * guess - x # 1 operation
        if diff == 0: #1
            return guess #1
        if diff < 0:  # our guess was lower than the true square root
            low = guess  # so we should continue searching in the range [guess - high]
        else:  # our diff was higher than the true square root
            high = guess  # we continue searching in the range [low - guess]

        if high - low <= 1:  # at this point we can't an integer square root for x
            break

        guess = (
                            low + high) // 2  # pick a guess in the middle of the new range
    return -1
