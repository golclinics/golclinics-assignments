/**
 * Returns idx of target, -1 if not found
 * @param nums - a sorted array of integers
 * @param target - integer to search for
 * @returns idx of target, -1 if not found
 */
function iterativeBinarySearch(nums: number[], target: number): number {
  let leftIdx = 0,
    rightIdx = nums.length - 1;

  while (leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2);

    if (nums[midIdx] === target) return midIdx;

    if (nums[midIdx] < target) {
      leftIdx = midIdx + 1;
    } else {
      rightIdx = midIdx - 1;
    }
  }

  return -1;
}

// Time - O(log(n))
// Space - O(1)

const numbers: number[] = [1, 3, 4, 5, 10, 11, 23, 50];
