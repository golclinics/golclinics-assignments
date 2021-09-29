const A = ["t", "h", "i", "s", " ", "i", "s", " ", "g", "o", "o", "d"];
// Intuition behind my solution :
// we start by reversing the whole sentence then reverse the indivisual words
function reverseSentence(A) {
  helperReverse(A, 0, A.length - 1);
  let startInd = 0;
  for (let i = 0; i <= A.length; i++) {
    if (A[i] === " " || i === A.length) {
      helperReverse(A, startInd, i - 1);
      startInd = i + 1;
    }
  }
  return A;
}

// helper function to implement reverse
function helperReverse(array, start, end) {
  while (start < end) {
    let temp = array[start];
    array[start] = array[end];
    array[end] = temp;
    start++;
    end--;
  }
}

console.log(reverseSentence(A));
