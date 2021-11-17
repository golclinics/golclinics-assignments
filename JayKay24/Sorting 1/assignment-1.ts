import {
  Comparator,
  LessThan,
  GreaterThan,
} from "./comparator";

/**
 * Determine if a collection is sorted
 *
 * @param integers - an array of integers
 * @param comparator - order criteria, descending or ascending
 *
 * @returns Boolean indicating if the array is sorted
 */
function isSorted(
  integers: number[],
  comparator: Comparator<number> = new GreaterThan()
): boolean {
  for (let i = 1; i < integers.length; i++) {
    if (!comparator.compare(integers, i, i - 1)) return false;
  }

  return true;
}
/**
 * Time - O(n)
 * Space - O(1)
 */

// is an empty list, by definition, sorted?

const gt = new GreaterThan();
const lt = new LessThan();
console.log(isSorted([3, 2, 1], gt)); // false
console.log(isSorted([3, 2, 1], lt)); // true
console.log(isSorted([1, 4, 2, 3], gt)); // false
