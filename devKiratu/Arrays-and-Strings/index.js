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

/**
2. Reverse Sentence In-place

Write a function reverseSentence(A) that takes in an array of characters, A, and reverses 
the the "words" (not individual characters).

Example:

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A)
A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
 */

function reverseSentence(s) {
	const wordArr = [...s].join("").split(" ");

	//reusing function from Q1 above
	reverseArray(wordArr);

	return wordArr.join(" ").split("");
}

const sentence = ["t", "h", "i", "s", " ", "i", "s", " ", "g", "o", "o", "d"];
console.log(reverseSentence(sentence));

//TODO Q3 - WIP

/**
4. Leetcode: Remove Element

URL - https://leetcode.com/problems/remove-element/
 */
/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function (nums, val) {
	let count = 0;
	for (let i = 0; i < nums.length; i++) {
		if (nums[i] === val) {
			nums[i] = "x";
			count++;
		}
	}
	nums.sort().splice(nums.indexOf("x"), count);
	return nums.sort().length;
};

console.log(removeElement([3, 2, 2, 3], 3));
//console.log(removeElement([0,1,2,2,3,0,4,2], 2))
