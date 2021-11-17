import { swap } from "./assignment-2";
import {
  GreaterThan,
  LessThan,
  Comparator,
} from "./comparator";

/**
 * Perform insertion sort on the array
 *
 * @param array - an array of integers
 * @param comparator - order criteria, descending or ascending
 *
 * @returns Sorted array
 */
function insertionSort(
  array: number[],
  comparator: Comparator<number> = new LessThan()
): number[] {
  let currentIdx = 1;

  while (currentIdx < array.length) {
    let i = currentIdx;
    let placeFound = false;

    while (i > 0 && !placeFound) {
      if (comparator.compare(array, i, i - 1)) {
        swap(array, i, i - 1);
        i--;
      } else {
        placeFound = true;
      }
    }

    currentIdx++;
  }

  return array;
}

/**
 * Time - O(n ^ 2)
 * Space - O(1)
 */

const gt = new GreaterThan();
const lt = new LessThan();
console.log(insertionSort([3, 2, 5], gt)); // [5, 3, 2];
console.log(insertionSort([3, 2, 5], lt)); // [2, 3, 5];
