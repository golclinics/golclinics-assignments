def merge_lists(nums, temp, left_start, right_end):
    middle = left_start + ((right_end - left_start) // 2)
    left_end = middle
    right_start = middle + 1

    right = right_start
    left = left_start
    index = left_start

    while left <= left_end and right <= right_end:
        if nums[left] <= nums[right]:
            temp[index] = nums[left]
            left += 1
        else:
            temp[index] = nums[right]
            right += 1

        index += 1

    # Copy in left over elements from left or right subarray
    if left > left_end:
        for i in range(right, right_end + 1):
            temp[index] = nums[i]
            index += 1
    else:
        for i in range(left, left_end + 1):
            temp[index] = nums[i]
            index += 1

    # Copy in sorted array from temp back into input array
    for i in range(left_start, right_end + 1):
        nums[i] = temp[i]


def merge_sort(nums: list, temp: list, left: int, right: int):
    if left >= right:
        return

    middle = left + ((right - left) // 2)

    merge_sort(nums, temp, left, middle)
    merge_sort(nums, temp, middle + 1, right)

    merge_lists(nums, temp, left, right)


def nums_sort(nums: list):
    size = len(nums)
    temp = [0] * size
    merge_sort(nums, temp, 0, size - 1)


# Tests
nums = [7, 3, 2, 8, 1, 5]
nums_sort(nums)
print(nums)
