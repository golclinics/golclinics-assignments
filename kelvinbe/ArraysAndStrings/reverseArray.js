`Write a function reverseArray(A) that takes in an array A and reverses it, 
without using another array or collection data structure; in-place.`



const reverseArray = (arr) => {
    for (var i = 0; i <= (arr.length / 2); i++) {
    let el = arr[i];
      arr[i] = arr[arr.length - 1 - i];
      arr[arr.length - 1 - i] = el;
    }
    return arr;
    }
    
console.log(reverseArray([1,2,3,4,5]))