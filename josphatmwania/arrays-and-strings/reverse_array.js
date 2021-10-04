//  1. Reverse Array In-place
// Write a function reverseArray(A) that takes in an array A and reverses it, without using another array or collection data structure; in-place.

// Example:

// A = [10, 5, 6, 9]
// reverseArray(A)
// A // [9, 6, 5, 10]


A = [10, 5, 6, 9];

Array.prototype.reverse.call(A);
console.log(A);


