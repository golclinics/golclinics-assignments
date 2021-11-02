/**
 * Returns idx of target, -1 if not found
 * @param nums - an array of integers
 * @param target - integer to search for
 * @param leftIdx - left index used to calculate midpoint
 * @param rightIdx - right index used to calculate midpoint
 * @returns idx of target, -1 if not found
 */
function recursiveBinarySearch(
  nums: number[],
  target: number,
  leftIdx: number = 0,
  rightIdx: number = nums.length - 1
): number {
  const midIdx = Math.floor((leftIdx + rightIdx) / 2);

  if (nums[midIdx] === target) return midIdx;
  if (leftIdx > rightIdx) return -1;

  let result = -1;

  if (nums[midIdx] < target) {
    result = recursiveBinarySearch(nums, target, midIdx + 1, rightIdx);
  } else {
    result = recursiveBinarySearch(nums, target, leftIdx, midIdx - 1);
  }

  return result;
}

const numbers: number[] = [1, 3, 4, 5, 10, 11, 23, 50];
