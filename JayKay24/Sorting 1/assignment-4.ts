/**
 * Performs mergesort on the array
 *
 * @param array - an array of integers
 *
 * @returns sorted array of integers
 */
function mergeSort(array: number[]): number[] {
  if (array.length < 2) return array;

  let midIdx = Math.floor(array.length / 2),
    leftArray = array.slice(0, midIdx),
    rightArray = array.slice(midIdx);

  return merge(mergeSort(leftArray), mergeSort(rightArray));
}

/**
 * Time - O(nLog(n))
 * Space - O(n)
 */

/**
 * Merges leftArr and rightArr and sorts the result
 *
 * @param leftArr - an array of integers
 * @param rightArr - an array of integers
 *
 * @returns merged leftArr and rightArr, sorted
 */
function merge(leftArr: number[], rightArr: number[]): number[] {
  const results: number[] = [];
  let leftIdx = 0,
    rightIdx = 0;

  while (leftIdx < leftArr.length && rightIdx < rightArr.length) {
    if (leftArr[leftIdx] < rightArr[rightIdx]) {
      results.push(leftArr[leftIdx++]);
    } else {
      results.push(rightArr[rightIdx++]);
    }
  }

  const leftRemains = leftArr.slice(leftIdx),
    rightRemains = rightArr.slice(rightIdx);

  return [...results, ...leftRemains, ...rightRemains];
}
