import { swap } from "./assignment-2";

/**
 * Perform insertion sort on the array
 *
 * @param array - an array of integers
 */
function insertionSort(array: number[]): number[] {
  let currentIdx = 1;

  while (currentIdx < array.length) {
    let i = currentIdx;
    let placeFound = false;

    while (i > 0 && !placeFound) {
      if (array[i] < array[i - 1]) {
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