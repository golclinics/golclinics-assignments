const SPACE = " ";

/**
 * Reverses the "words" (not individual characters) in-place
 * @param {string[]} wordsList - an array of characters representing words
 * @returns {string[]} modified, reversed wordsList array
 */
function reverseSentence(wordsList: string[]): string[] {
  // intitial reversal
  reverseSentenceInPlace(wordsList, 0, wordsList.length - 1);

  let wordStart = 0;

  for (let i = 0; i < wordsList.length; i++) {
    while (wordsList[wordStart] === SPACE) wordStart++;

    if (i > wordStart) {
      if (wordsList[i] === SPACE) {
        reverseSentenceInPlace(wordsList, wordStart, i - 1);
        wordStart = i;
      } else if(i + 1 >= wordsList.length && wordsList[i] !== SPACE) {
        reverseSentenceInPlace(wordsList, wordStart, i);
      }
    }
  }

  return wordsList;
}

/**
 * Reverse parts of arr in-place
 * @param {string[]} arr - an array of characters
 * @param {number} idx1 - first idx to begin reversal
 * @param {number} idx2 - second idx to end reversal
 */
function reverseSentenceInPlace(
  arr: string[],
  idx1: number,
  idx2: number
): void {
  let leftIdx = idx1,
    rightIdx = idx2;

  while (leftIdx < rightIdx) {
    swap(arr, leftIdx, rightIdx);
    leftIdx++;
    rightIdx--;
  }
}

/**
 * Swap items in idx1 with idx2
 * @param {string[]} arr - an array of characters to perform swap
 * @param {number} idx1 - swap item at index idx1 with idx2
 * @param {number} idx2 - swap item at index idx2 with idx1
 */
function swap(arr: string[], idx1: number, idx2: number): void {
  [arr[idx2], arr[idx1]] = [arr[idx1], arr[idx2]];
}

const A = ["t", "h", "i", "s", " ", "i", "s", " ", "g", "o", "o", "d"];
reverseSentence(A);
// A = ['g','o','o','d',' ','i','s',' ','t','h','i','s'];
