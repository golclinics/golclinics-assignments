#implementing a function that sums elements to a given target
def sumTarget(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i,j]

print(sumTarget([2,7,11,15],9))