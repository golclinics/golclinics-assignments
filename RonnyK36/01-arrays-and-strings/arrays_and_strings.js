// 1. Reverse Array In-place
// Write a function reverseArray(A) that takes in an array A
// and reverses it, without using another array or collection data structure;
// in-place.

var A = [1, 2, 3, 4, 5, 6, 7];

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


// 2. Reverse Sentence In-place
// Write a function reverseSentence(A) that takes in an array of characters, A,
// and reverses the the "words" (not individual characters).

var B = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'];

function reverseSentence(B) {

    for (var i = 0, j = B.length - 1; i < B.length / 2; i++, j--) {
        var temp = B[i];
        B[i] = B[j];
        B[j] = temp;
    }

    console.log('ASSN 2 - Reverse sentence:');
    console.log(B);
    return B;
}

reverseSentence(B);