/*Write a function reverseArray(A) that takes in an array A and reverses it,
without using another array or collection data structure; in-place.*/

const A = [10, 5, 6, 9];

function reverseArray(arr){
    for(let i =0, j=arr.length -1; i<arr.length/2; i++,j--){
        
        let tempValue = arr[i];
        arr[i]= arr[j];
        arr[j]=tempValue;
        // console.log(arr);
        
    }
    console.log(arr);
    return arr;

}

reverseArray(A);





