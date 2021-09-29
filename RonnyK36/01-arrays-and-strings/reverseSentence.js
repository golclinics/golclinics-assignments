// 2. Reverse Sentence In-place
// Write a function reverseSentence(A) that takes in an array of characters, A,
// and reverses the the "words" (not individual characters).

const A = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'];


function reverseSentence(A) {

    // reverse words
    reverseBySwap(A, 0, A.length - 1);
    let startInd = 0;
    for (let i = 0; i <= A.length; i++) {
        if (A[i] === ' ' || i === A.length) {
            // reverse strings in place
            reverseBySwap(A, startInd, i - 1);
            startInd = i + 1;
        }
    }
    console.log('ASSN 2 - Reverse Sentence: ');
    console.log(A);
    return A;
}


// reverse by Swapping the whole sentence
function reverseBySwap(array, start, end) {
    while (start < end) {
        let temp = array[start];
        array[start] = array[end];
        array[end] = temp;
        start++;
        end--;
    }
}


reverseSentence(A);