/**
 * Takes in an array of items and reverses it in-place
 * @param items - an array of items
 * @returns items - original array
 */
function reverseArray<T>(items: T[]): T[] {
  let leftIdx = 0,
    rightIdx = items.length - 1;

  while (leftIdx < rightIdx) {
    swap<T>(items, leftIdx, rightIdx);
    leftIdx++;
    rightIdx--;
  }

  return items;
}

/**
 * Swap item at idx1 with item at idx2
 * @param {T[]} arr - an array of items
 * @param {number} idx1 - swap item at index idx1 with item at idx2
 * @param {number} idx2 - swap item at index idx2 with item at idx1
 */
function swap<T>(arr: T[], idx1: number, idx2: number): void {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const A = [10, 5, 6, 9];
console.log(reverseArray<number>(A));
// A = [9, 6, 5, 10]