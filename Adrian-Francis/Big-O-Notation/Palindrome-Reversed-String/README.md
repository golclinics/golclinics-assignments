This solves the palindrome problem stated above by comparing the original string with the reversed version of the string:

```
def is_palindrome_rev(s):
    reversed_s = s[::-1] # This is a neat trick to reverse a string in python
    return s == reversed_s

```

The above method uses the fancy slicing feature in Python [::-1] which reverses a sequence. The following implementation

```
def is_palindrome_rev2(s):
    reversed_seq = reversed(s) # creates a sequence with the characters in the string in reverse
    reversed_s = ''.join(reversed_seq) # transformed the reversed sequence into a string
    return s == reversed_s

```