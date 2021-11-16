/**
 * Swap two integers in the array
 *
 * @param array - an array of integers
 * @param idx1 swap array[idx1] with array[idx2]
 * @param idx2 swap array[idx2] with array[idx1]
 */
function swap(array: number[], idx1: number, idx2: number): void {
  [array[idx2], array[idx1]] = [array[idx1], array[idx2]];
}
