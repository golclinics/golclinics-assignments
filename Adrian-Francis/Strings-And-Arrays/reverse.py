# This is more efficient in reversing an array in place
# Big-O notation: ?

def reverse(A):
    print(list(reversed(A)))

reverse([1, 2, 3, 4])
assert reverse([1, 2, 3, 4] == [4, 3, 2, 1])
