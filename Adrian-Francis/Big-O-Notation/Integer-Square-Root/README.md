Given a positive integer number x which has an integer square root, the int_sqrt(x) returns the square root of x. If x does not have a square root, the function returns -1.

E.g. int_sqrt(16) -> 4, int_sqrt(10) -> -1

```
def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1

```