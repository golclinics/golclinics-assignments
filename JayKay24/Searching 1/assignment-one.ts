type TargetSumPair = [number, number];

/**
 * Returns indices of two numbers such that they add up to target
 * @param nums - An array of integers
 * @param target
 *
 * @returns Indices of two numbers in nums that add up to target
 */
function findIdxs(nums: number[], target: number): TargetSumPair {
  const idxs: TargetSumPair = [-1, -1];
  const seen: Map<number, number> = new Map();

  for (let i = 0; i < nums.length; i++) {
    const current = nums[i];
		
    if (seen.has(current)) {
      idxs[0] = seen.get(current);
      idxs[1] = i;
      break;
    }

    const result = target - current;
    seen.set(result, i);
  }

  return idxs;
}
