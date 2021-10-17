// Reverse the words
function reverse(A,first,last)
{
   
    let temp;        
     
    while (first <= last)
    {
        // Swapping the first and last character
        temp = A[first];
        A[first]=A[last];
        A[last]=temp;
        first++;
        last--;
    }
}
// Function to reverse words

function reverseSentence(A)
{
    // Reversing individual words
       
    let first = 0;
    for (let last = 0; last < A.length; last++)
    {
        // If we see a space, we
        // reverse the previous
        // word (word between
        // the indexes first and last-1
       
                    if (A[last] == ' ')
        {
            reverse(A, first, last);
            first = last + 1;
        }
    }
    // Reverse the last word
    reverse(A, first, A.length - 1);
     
    // Reverse the entire String
    reverse(A, 0, A.length - 1);
    return A;
}
// testcase

 let A = ['t','h','i','s',' ','i','s',' ','g','o','o','d'];
 //let A = ['i',' ','a',' m',' ','g','o','o','d'];

//console.log(reverse(A));
console.log(reverseSentence(A));