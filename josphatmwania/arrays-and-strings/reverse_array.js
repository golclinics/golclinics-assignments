//  1. Reverse Array In-place
// Write a function reverseArray(A) that takes in an array A and reverses it, without using another array or collection data structure; in-place.

// Example:

// A = [10, 5, 6, 9]
// reverseArray(A)
// A // [9, 6, 5, 10]






function reverseArray(A) {
	let m = 0;
	for (let i = A.length - 1; i >= m; i--) {
		let a = A[m];
		A[m] = A[i];
		A[i] = a;
		m++;
	}
	return A;
}
// Given Array
const Array = [10, 5, 6, 9];

console.log(`${Array} the reversed is: ${reverseArray(Array)}`);