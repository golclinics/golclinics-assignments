import { Comparator, LessThan } from "./comparator";

/**
 * Perform insertion sort on the array
 *
 * @param array - an array of items
 * @param comparator - order criteria, descending or ascending
 *
 * @returns Sorted array
 */
export function insertionSort<T>(
  array: T[],
  prop: string,
  comparator: Comparator<T> = new LessThan()
): T[] {
  let currentIdx = 1;

  while (currentIdx < array.length) {
    let i = currentIdx;
    let placeFound = false;

    while (i > 0 && !placeFound) {
      if (comparator.compare(array, i, i - 1, prop)) {
        swap<T>(array, i, i - 1);
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
 * Swap two items in the array
 *
 * @param array - an array of items
 * @param idx1 swap array[idx1] with array[idx2]
 * @param idx2 swap array[idx2] with array[idx1]
 */
export function swap<T>(array: T[], idx1: number, idx2: number): void {
  [array[idx2], array[idx1]] = [array[idx1], array[idx2]];
}
