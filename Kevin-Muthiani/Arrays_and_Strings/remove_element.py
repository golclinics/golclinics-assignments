# https://leetcode.com/problems/remove-element/
# Given an array nums and a value val, remove all instances of that value 
# in-place and return the new length. Do not allocate extra space for another 
# array, you must do this by modifying the input array in-place with O(1) 
# extra memory. The order of elements can be changed. It doesn't matter what 
# you leave beyond the new length.

def removeElement(nums, val):
    n = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[n] = nums[i]
            n += 1
        
    return n


# Test function
if __name__ == "__main__":
    myArray = [3, 2, 2, 3]
    value = 3
    result = removeElement(myArray, value)
    print(result)
    print(myArray)