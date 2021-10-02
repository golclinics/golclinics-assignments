// # Return minimun swap count to guarantee no repeating numbers are sorted
// [4,2,1,3]
// swap = 0;
// From index = 0 to end of array
    // while value at index is not index +1  // !1
        // hopeIndex = A[index]-1 //3
        // temp = A[index]
        // A[index] = A[hopeIndex] // A[3]
        // A[hopeIndex] = temp
        // increase swap count
    // end while
// end for
// console log array
// console swap count

function swapCount(A) {
    let swapCount = 0;
    for (let i= 0; i < A.length; i ++) {
        while (i + 1 != A[i]) {
            let hopeIndex = A[i] - 1;
            let temp = A[i]
            A[i] = A[hopeIndex];
            A[hopeIndex] = temp;
            swapCount ++;
        }
    }
    console.log(swapCount)
    console.log(A)
}

swapCount([2,8,5,4])