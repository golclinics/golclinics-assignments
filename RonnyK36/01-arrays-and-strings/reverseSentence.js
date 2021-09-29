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