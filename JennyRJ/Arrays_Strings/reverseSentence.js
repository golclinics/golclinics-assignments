/*Write a function reverseSentence(A) that takes in an array of characters, A,
and reverses the the "words" (not individual characters).*/


const arr = ['t','h','i','s',' ','i','s',' ','g','o','o','d'];


function reverseSentence(arr){
    reverseItems(arr,0, arr.length-1);
    var index= 0;
    for(let i = 0; i<=arr.length; i++){
        if(arr[i] === ' ' || i===arr.length){
            reverseItems(arr, index, i-1);
            index=i+1;
        }
    }
    console.log(arr);
     
    return arr;
}

function reverseItems(arrayToReverse, start, end){

    while(start < end){
       let tempValue = arrayToReverse[start];
       arrayToReverse[start]= arrayToReverse[end];
       arrayToReverse[end]= tempValue;
       start++;
       end--; 
    }
}

reverseSentence(arr);