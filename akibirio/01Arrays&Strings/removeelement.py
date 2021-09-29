from typing import List


class Solution:
    def removeElement(nums: List[int], val: int) -> int:
        list_length = len(nums)
        k = 0

        for i in range(list_length):
            if nums[i] == val:
                nums[i] = -1

            else:
                k += 1

        start, end = 0, list_length - 1
        while start < end:
            if nums[start] != -1:
                start += 1
            else:
                while nums[end] == -1 and end >= 1 and start < end:
                    end -= 1
                # now nums[end] > -1
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return k


if __name__ == '__main__':
    nums = [3,2,2,3]
    print(Solution.removeElement(nums, 3))
