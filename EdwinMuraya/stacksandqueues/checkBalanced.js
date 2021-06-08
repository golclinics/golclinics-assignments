const Stack = require("./stack");
// Examples To understand the Problem
// Assumption
// The input string only contain {[()]}
// Note
// A bracket is not balanced if the set of brackets it encloses are not matched.


const a = checkBalanced("[[[]]]"); // true
const b = checkBalanced("[([({})])]"); // true
const c = checkBalanced("[({]})]"); // false
const d = checkBalanced("{[(])}"); // false
// pseudocode
// create a stack of length of input string
// for every char in the string
   // push all the opening brackets
   // if you encounter a closing bracket 
      // compare the bracket, with what is on top of stack to see if match
      //   if match pop out the top element
      //   if not match break out (not balanced) return false
// return true

function checkBalanced(str) {
    // using the stack I had created
    let stack = new Stack(str.length);

    for (var char of str) {
        if (char === "[" || char === "(" || char === "{") stack.push(char);
        else if (char === "}" || char === ")" || char === "]") {
            if (char === "]") {
                if (stack.peek() === "[") stack.pop();
                else return false;
            }
            if (char === ")") {
                if (stack.peek() === "(") stack.pop();
                else return false;
            }
            if (char === "}") {
                if (stack.peek() === "{") stack.pop();
                else return false;
            }
        }
    }
    return true;
}

console.log("true", b);
console.log("false", c);
console.log("false", d);

// Discussion
// The Space Complexity of the function is O(n) since I create a stack equal to
// size of the input string.
//
// The time complexity is O(n), Number of operation equally to the increase or
// decrease in the size of the input string.
