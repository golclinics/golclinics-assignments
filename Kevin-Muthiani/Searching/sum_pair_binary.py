# Given an array of integers and an integer target,
# return indices of the two different elements that sum up to the target.
# Assume that each input would has exactly one solution.

from typing import List, Tuple

# Time - O(log(n)), Space - O(log(n)); n = size of nums
def binary_search_num(nums, target, first, last):
    """
    Helper function that iteratively searches for target in list of nums
    :param nums: list of numbers in ascending order
    :param target: search target
    :param first: first index to consider
    :param last: last index to consider
    :return: index of target in nums or -1 if not found
    """

    if (first > last):
        return -1

    mid = first + ((last - first) // 2)
    mid_value = nums[mid]

    if mid_value == target:
        # Match
        return mid
    elif nums[mid] > target:
        # Eliminate right side of array
        last = mid - 1
    else:
        # Eliminate left side of array
        first = mid + 1

    return binary_search_num(nums, target, first, last)


# Time - O(n*log(n)), Space - O(n*log(n)); n = size of nums
def get_array_pair(nums: List[int], target: int) -> List[int]:
    first = 0
    last = len(nums) - 1

    for first_num_index in range(len(nums)):
        search_target = target - nums[first_num_index]
        second_num_index = binary_search_num(nums, search_target, first, last)
        if second_num_index != -1:
            return [first_num_index, second_num_index]

    return []


# Tests
nums = [2,7,11,15]
print(get_array_pair(nums, 9))

nums = [2,3,4]
print(get_array_pair(nums, 6))

nums = [3,3]
print(get_array_pair(nums, 6))