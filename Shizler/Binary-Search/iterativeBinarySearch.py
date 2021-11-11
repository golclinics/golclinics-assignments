def iterativeBinarySearch(nums,target):
    rightIdx = len(nums) - 1
    leftIdx = 0
    while leftIdx <= rightIdx:
        midIdx = ((leftIdx + rightIdx) // 2)

        if nums[midIdx] == target: return target
        if target < nums[midIdx]:
            rightIdx = midIdx - 1
        else:
            leftIdx = midIdx + 1
        
    return -1
nums= [1, 3, 4, 5, 10, 11, 23, 50]

print(iterativeBinarySearch(nums,10))