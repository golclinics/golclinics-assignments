Given an array A and a distance d, the rotate_left function moves every element in A d steps to the left. Items will be cycled back to the end if they pass beginning.

For example, let A = [3, 2, 1, 10, 15, 3] and d = 3, then rotate_left(A, d) will result in the following array: [10, 15, 3, 3, 2, 1]

```
def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item


```