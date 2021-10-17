# Palindrome using reversed string

This solves the palindrome problem stated above by comparing the original
string with the reversed version of the string:

```python
def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s
```

The above method uses the fancy slicing feature in Python `[::-1]` which reverses
a sequence. The following implementation

```python
def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s
```

## Time Complexity

**O(n)** - The string reverse functions used in both implementations run in `O(n)` time. In `is_palindrome_rev2`, there is an additional `join` function that also runs in `O(n)` time. This causes it to have a time complexity of `O(2n)`, but we drop the constants, therefore it runs in linear time.

## Space Complexity

**O(n)** - In `is_palindrome_rev`, a new variable that contains the reversed string is created. The size of the reversed string is directly proportional to the input string, so it increases as the input increases. The `is_palindrome_rev2` on the other hand first creates a new array of size `n`, then a new string of size `n`, causing the space complexity to be `O(2n)`, but we drop the constants, so both implementations take up `O(n)` space