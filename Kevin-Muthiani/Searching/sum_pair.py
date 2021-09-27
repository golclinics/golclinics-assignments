# Given an array of integers and an integer target,
# return indices of the two different elements that sum up to the target.
# Assume that each input would has exactly one solution.

from typing import List, Tuple

# Using arrays only; Time - O(n^2), Space - O(1)
def get_array_pair(nums: List[int], target: int) -> List[int]:

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return [i, j]

    return []


# Using hashing; Time - O(n), Space - O(n)
def get_array_pair_2(nums: List[int], target: int) -> List[int]:
    nums_index: dict = {}

    for i in range(len(nums)):
        num = nums[i]
        if (target - num) in nums_index:
            return [ nums_index[target - num], i ]
        else:
            nums_index[num] = i

    return []


# Tests
nums = [2,7,11,15]
print(get_array_pair(nums, 9))
print(get_array_pair_2(nums, 9))

nums = [3,2,4]
print(get_array_pair(nums, 6))
print(get_array_pair_2(nums, 6))

nums = [3,3]
print(get_array_pair(nums, 6))
print(get_array_pair_2(nums, 6))