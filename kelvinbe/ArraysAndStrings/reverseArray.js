`Write a function reverseArray(A) that takes in an array A and reverses it, 
without using another array or collection data structure; in-place.`



const reverseArray = (a) => {
    let b = []
    
    for(let i = a.length-1; i>=0; i--){
        b.push(a[i]);
    }
    console.log(b)
    }
    
reverseArray([1,2,3,4,5])