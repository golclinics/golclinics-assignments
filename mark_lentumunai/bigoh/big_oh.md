# Analysis of Time and Space Complexities

## Countdown

Given an integer `n` as input `countdown(n)` prints the numbers n to 1 in descending
order then prints "Blast off!"

```python
## How many times can a number be divide by 2 until we get to 1
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Blast off!")
```

### solution

For the above function(countdown(n)) that prints the numbers in descending order
its runtime complexity(worst case) is O(n)
while it's space complexity is constant O(1)

## Countdown recursive

This solves the same problem as the previous algorithm, but uses recursion instead of a loop.
This might not be obvious if you're not familiar with function call stacks. Bonus points
if you can explain why the space complexity here is not the same as the space complexity
of the loop-based implementation. Feel free to research on the Internet.

```python
def countdown_recursive(n):
    #1 operation
    if n == 0:
        #1 operation
        print("Blast off")
    else:
        #1 operation
        print(n)
        countdown_recursive(n - 1)
```
### solution
for a recursive function, the time complexity (worst_case) is O(n)
    taking T(n)- total operations, and assuming each operation to cost 1 i.e T(0) = 1 if n > 0
    T(n) = T(n-1) + 3
    T(n) = T(n-2) + 6
    T(n) = T(n-2) + 9
    .
    .
    T(n) = T(n-k) + 3k
    n-k = 0 implying n = k
    T(n) = T(0) - 3n
    T(n) = 1 + 3n
    bigO = O(n)

in terms of the space complexity it can be expressed as O(n) as an implicit stack will be formed depending on the input size

## Palindrome

Given a string `s` as input, the `is_palindrome(s)` function returns true if `s` is a palindrome
and returns false otherwise. A palindrom in this case is a word that reads the same forward and
backwards, e.g. `madam`

```python
def is_palindrome(s):
    #1 operation
    if len(s) == 0:
        # single operation
        return True   # an empty string is a palindrome
    #2 operations
    size = len(s)
    #2 operations
    midpoint = size // 2
    #4 operations * n
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    # single operation
    return True
```
### solution
 total operations are 7 + 4n hence time complexity is O(7 + 4n)
 time complexity - O(n)
 space complexity is constant that is O(1)


## Palindrome using reversed string

This solves the palindrome problem stated above by comparing the original
string with the reversed version of the string:

```python
def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s
```

### solution
the above has a constant time complexity O(1), proved by timing it as the input grows bigger
and also constant space O(1)

```python
def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s
```

### solution
the above has a runtime and space complexity of O(n)

## Palindrome using recursion

This implementation is similar to the loop-based version in that it compares a pair of letters
at equal distances from the middle of the string in each iteration. But it does so using
recursion instead of a loop:

```python
def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    
    # in python s[-1] is the last element of the sequence s, i.e. "madam"[-1] -> "m"
    # and s[1: -1] will create a slice starting from the second element to the second last element
    # "madam"[1: -1] -> "ada"
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])
```

### solution
the above has a time complexity(worst_case) of O(n)
also the space complexity is (O)n

**Bonus questions**:

- Between `is_palindrome`, `is_palindrome_rev` and `is_palindrome_recur` which do you think is more efficient, and why?
- Which of the two implementations would you prefer for your own code, and why?

## solution
    is_palindrome_rev is more efficient because of its time and space complexities, though it utilizes python inbuilt method to reverse a string or an array

    in terms of time and space complexities being the metrics then, i would go for is_palindrome_rev

## Concatenating arrays

Given 2 arrays A and B of size m and n respectively, return a new array that contains the elements of the first array followed
by the elements of the second array.

This might not be immediately obvious. Bare in mind that in this example we have to inputs we care about so we have to consider
how an increase in either `m` or `n` affects the size of the `result` or the total number of iterations performed by the function.

For this example, let's assume that `result.append()` is a constant-time operation.

```python

def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result
```

### solution:
the time complexity of the above problem is O(n)
while the space complexity is O(n)

## Rotate an array to the left by a certain amount

Given an array A and a distance `d`, the `rotate_left` function moves every element in `A` `d` steps to the left.
Items will be cycled back to the end if they pass beginning.

For example, let A = [3, 2, 1, 10, 15, 3] and d = 3, then `rotate_left(A, d)` will result in the following array:
`[10, 15, 3, 3, 2, 1]`

```python
def rotate_left(A, d):
    for _ in range(d):
        #2 operations
        first_item = A[0]
        for i in range(len(A)):
            #3 operations
            A[i] = A[i + 1]
        # single operation
        A[-1] = first_item

```
### solution
Time complexity (Worst case) - O(n**2)
space complexity (Worst case) - O(1)


## How many times can a number be divide by 2 until we get to 1

The `count_div_2(n)` functions counts the number of times the input number
`n` can be divided by 2 before it reaches one or less.

The time complexity may not be immediately obvious to all, but here's a hint:
Count the number of iterations that this functions makes when then input is 4, 5, 6, 7, 8.
At which values of `n` does the number of iterations increase compared to when `n = 4`?
Now keep trying for values > 8, at which point does the number of iterations increase by 1 compared
to when `n=8`? Do you see a pattern or trend between the growth in `n` and how that affects
the increase in iterations? In general, how much should `n` grow before count increases by 1? Do you
see a mathematical releationship `n` and the total number of iterations?

```python
def count_div_2(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
```
### solution
Time complexity is O(log(n))
space complexity is O(1)

## Integer square root

Given a positive integer number `x` which has an integer square root, the `int_sqrt(x)` returns
the square root of x. If `x` does not have a square root, the function returns `-1`.

E.g. `int_sqrt(16)` -> `4`, `int_sqrt(10)` -> -1

```python
def int_sqrt(x):
    for i in range(x):
        # 2 operations
        if i * i == x:
            # single operation
            return i
    
    return -1
```
### solution
Time complexity is O(n)
space complexity is O(1)


## Integer square root bisection method

This solves the same problem as `int_sqrt` using a different approach:
instead of trying out all numbers from 0-x, it tries out the number in the middle
of the range, then eliminates half of the range where it's sure the answer cannot be found
then keep repeating that process until the answer is found.


```python
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
### solution
the above problem has a runtime complexity of O(n) and constant space complexity of O(1)
