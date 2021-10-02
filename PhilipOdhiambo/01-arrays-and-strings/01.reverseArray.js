

// o(n) sapace complexity

// 1. swap first-place with last-place
// 2. Increase first-place and decrease last-place
// 3. Repeat from 1: until first-place equals last-place
function reverseArray(A) {
    let firstPlace = 0;
    let lastPlace = A.length-1;
    while(firstPlace < lastPlace) {
        let temp = A[lastPlace];
        A[lastPlace] = A[firstPlace];
        A[firstPlace] = temp;
        firstPlace ++;
        lastPlace --;
    }
    return A;
}

const test1 = reverseArray([1,2,3,4]);
const test2 = reverseArray([1,2,3,4,5]);

console.log(test1);
console.log(test2);


