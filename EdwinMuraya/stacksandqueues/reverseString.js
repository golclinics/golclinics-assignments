const Stack = require("./stack");

// concrete examples: showing input and output
const a = reverseString("Edwin"); // niwdE
const b = reverseString("this is kenya"); // aynek si sith

//Assumption
// We are reversion the string characterwise

// Pseudocode
// create new string for reversion.(since string are immutable. you can't reverse inplace)
// create stack of the length of string
// for every char in the string:
// push each element in the stack
// for every char in the stack
// pop out a from stack to the new string
// return the new string(reversed)

function reverseString(str) {
    let reverse = [];
    const stack = new Stack(str.length);
    for (var char of str) {
        stack.push(char);
    }
    for (var i = 0; i < str.length; i++) {
        reverse[i] = stack.pop();
    }
    return reverse;
}

console.log(a);
console.log(b);

// Discussion
// Space Complexity of the function is O(2n). we can drop the 2 > simple O(n)
// since we are creating a new string of the same length as the input string,
// also creating a stack of the same length as the input string. Space will
// change linearly.

// Time complexity is also O(2n) since we are intrested the trend we can also
// drop the 2 to simplfy to O(n). This is because we have 2 consecultive for
// loops which number of operation is dependent on the input length.
