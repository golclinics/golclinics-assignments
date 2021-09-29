//reverseArray(A) that takes in an array A and reverses it
function reverseArray (a) {
    var newArr = [];
    for (var i = 0, j = a.length - 1; i < a.length; i++, j--) {      
        newArr[i] = a[j];
    }   
    return newArr;
}
console.log(reverseArray([10,5,6,9]));
    