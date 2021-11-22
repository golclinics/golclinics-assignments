# implement a function to check a collection is sorted
# checking if array is sorted in ascending order

def isSorted(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return True
    
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

print(isSorted([1,2,2,4,3]) )