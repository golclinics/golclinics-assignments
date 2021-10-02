/*
Reverse Sentence In-place:
Write a function reverseSentence(A) that 
takes in an array of characters, A, and 
reverses the the "words" (not individual characters).

Example:
A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']

reverseSentence(A)
A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
*/

// Psedo code
//1.reverse the whole sentence
//2.reverse back individual words

function reverseSentence(sentence) {
    //1.reverse the whole sentence
    let start = 0;
    let end = sentence.length - 1;
    reverse(sentence,start,end); //  setence['d','l','r','o','w','','o','l','l','e','h']

    //2.reverse back individual words
    let lBound = 0
    for (let i = 0; i <= sentence.length; i ++) {
        if (sentence[i] == " ") {
            let uBound = i-1;
            reverse(sentence,lBound,uBound);
            lBound = i + 1
        }

        if (i == sentence.length) {
            let uBound = sentence.length - 1
            reverse(sentence,lBound,uBound)
        }
    }

    // Function reverse
    function reverse(A,start,end) {
        while (start <= end) {
            let temp = A[start];
            A[start] = A[end];
            A[end] = temp;
            start ++;
            end --;
        }
    }

    console.log(sentence);
}

reverseSentence(['t','h','i','s',' ','i','s',' ','g','o','o','d']);