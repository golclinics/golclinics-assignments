// Hackerrank did not support Typescript for this challenge

/**
 * Returns minimum number of swaps required to sort the arrray in ascending
 * order
 * @param {object} arr - an unordered array of integers
 * @returns {number} minimum number of swaps to order the array
 * in ascending order
 */
function minimumSwaps(arr) {
  let minSwaps = 0;

  for (let i = 0; i < arr.length; i++) {
    while (arr[i] !== arr[arr[i] - 1]) {
      swap(arr, i, arr[i] - 1);
      minSwaps++;
    }
  }

  return minSwaps;
}

/**
 * Swap item at idx1 with item at idx2
 * @param arr - an array of integers
 * @param {number} idx1 - swap item at index idx1 with item at idx2
 * @param {number} idx2 - swap item at index idx2 with item at idx1
 */
function swap(arr, idx1, idx2) {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const integers = [7, 1, 3, 2, 4, 5, 6];
console.log(minimumSwaps(integers)); // 5
