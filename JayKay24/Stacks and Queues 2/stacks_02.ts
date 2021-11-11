import { Stack } from "./stack";

/**
 * Reads in a string and reverses it using a Stack push
 * and pop operations
 * @param str - string to reverse
 * @returns The reverse of str
 */
function reverseString(str: string): string {
  const stack = new Stack<string>("");
  let reversedStr = "";

  for (const char of str) {
    stack.push(char);
  }

  while (!stack.empty) {
    reversedStr += stack.peek();
    stack.pop();
  }

  return reversedStr;
}
