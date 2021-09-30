/** 
1. Reverse Array In-place

Write a function reverseArray(A) that takes in an array A and reverses it, without using another array or collection data structure; in-place.

Example:

A = [10, 5, 6, 9]
reverseArray(A)
A // [9, 6, 5, 10]
 */

function reverseArray(arr) {
	let j = 0;
	for (let i = arr.length - 1; i >= j; i--) {
		let a = arr[j];
		arr[j] = arr[i];
		arr[i] = a;
		j++;
	}
	return arr;
}

const testArray = [10, 5, 6, 9];
console.log(`${testArray} reversed is: ${reverseArray(testArray)}`);
