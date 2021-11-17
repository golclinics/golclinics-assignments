/**
 * Determine if a collection is sorted
 *
 * @param integers - an array of integers
 * @param ascending - order criteria, true for ascending, false for descending.
 * Default - ascending order
 *
 * @returns Boolean indicating if the array is sorted
 */
function isSorted(integers: number[], ascending = true): boolean {
  for (let i = 1; i < integers.length; i++) {
    if (ascending) {
      if (integers[i] < integers[i - 1]) return false;
    } else {
      if (integers[i] > integers[i - 1]) return false;
    }
  }

  return true;
}
/**
 * Time - O(n)
 * Space - O(1)
 */

// is an empty list, by definition, sorted?
