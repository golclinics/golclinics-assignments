// 1. Reverse Array In-place
// Write a function reverseArray(A) that takes in an array A
// and reverses it, without using another array or collection data structure;
// in-place.

const A = [1, 2, 3, 4, 5, 6, 7];

// reverse array function
function reverseArray(A) {
    let i = 0;
    let j = A.length - 1;
    for (i = 0; i < A.length / 2; i++, j--) {
        let temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
    console.log('ASSN 1 - Reverse array: ');
    console.log(A);
    return A;
}

reverseArray(A);