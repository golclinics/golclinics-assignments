# https://www.hackerrank.com/challenges/minimum-swaps-2/problem
# You are given an unordered array consisting of consecutive integers 
# [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any 
# two elements. Find the minimum number of swaps required to sort the 
# array in ascending order.


def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    valueIndexDict = dict(zip(arr, range(1, n+1)))
    
    for i in range(1,n+1):
        if valueIndexDict[i] != i:
            # Swap
            valueIndexDict[arr[i-1]] =  valueIndexDict[i]
            arr[valueIndexDict[i]-1] = arr[i-1]
            swaps += 1    
    
    return swaps


# Test function
if __name__ == "__main__":
    myArray = [4, 3, 1, 2]
    print(minimumSwaps(myArray))