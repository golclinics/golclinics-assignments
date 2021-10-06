# O(m + n) time | O(m + n) space
def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result
