/**
 * Determine if a collection is sorted
 * @param integers - an array of integers
 * @param ascending - order criteria, true for ascending, false for descending
 *
 * @returns Boolean indicating if the array is sorted
 */
function isSorted(integers: number[], ascending = true): boolean {
  for (let i = 0; i < integers.length; i++) {
    if (i > 0) {
      if (ascending) {
        if (integers[i] < integers[i - 1]) return false;
      } else {
        if (integers[i] > integers[i - 1]) return false;
      }
    }
  }

  return true;
}
// is an empty list, by definition, sorted?
