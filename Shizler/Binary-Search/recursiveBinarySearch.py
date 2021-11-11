def recursiveBinarySearch(nums,target,leftIdx,rightIdx):
    midIdx = (leftIdx + rightIdx) // 2

    if nums[midIdx] == target: return target
    if leftIdx > rightIdx: return -1

    result = -1
    if target < nums[midIdx]:
       result = recursiveBinarySearch(nums,target,leftIdx,midIdx - 1)
    else:
        result = recursiveBinarySearch(nums,target,midIdx + 1,rightIdx)
    return result
nums = [1, 3, 4, 5, 10, 11, 23, 50]

print(recursiveBinarySearch(nums,10,0,len(nums)-1))