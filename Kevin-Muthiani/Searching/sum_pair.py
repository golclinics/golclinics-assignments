# Given an array of integers and an integer target,
# return indices of the two different elements that sum up to the target.
# Assume that each input would has exactly one solution.

from typing import List, Tuple


def get_array_pair(nums: List[int], target: int) -> Tuple[int]:

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (nums[i] + nums[j]) == target:
                return i, j


# Tests
nums = [2,7,11,15]
target = 9
pair = get_array_pair(nums, target)
print(pair)

nums = [3,2,4]
target = 6
pair = get_array_pair(nums, target)
print(pair)

nums = [3,3]
target = 6
pair = get_array_pair(nums, target)
print(pair)