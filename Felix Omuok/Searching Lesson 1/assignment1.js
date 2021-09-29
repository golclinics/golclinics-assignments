/* 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9 Output: [0,1] Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6 Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6 Output: [0,1] */


const addUptoTarget = (arr, target) =>{
    for (let i = 0; i < arr.length; i++) {
        for (let j = i+1; j < arr.length; j++) {
            if(arr[i] + arr[j] === target) return [i,j];

        }

    }

    return false;
}
console.log(addUptoTarget([2,7,11,15], 9)); // [0,1]
console.log(addUptoTarget([3,2,4], 6)); // [1,2]
console.log(addUptoTarget([3,3], 6)); // [0,1]
