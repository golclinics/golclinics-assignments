Given 2 arrays A and B of size m and n respectively, return a new array that contains the elements of the first array followed by the elements of the second array.

This might not be immediately obvious. Bare in mind that in this example we have to inputs we care about so we have to consider how an increase in either m or n affects the size of the result or the total number of iterations performed by the function.

For this example, let's assume that result.append() is a constant-time operation.

```

def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result

```