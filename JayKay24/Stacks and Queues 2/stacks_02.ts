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

/**
 * Returns "YES" if brackets is balanced, "NO" if unbalanced
 * @param brackets - a sequence of brackets
 * @param "YES" if brackets is balanced, "NO" if unbalanced
 */
function balancedBrackets(brackets: string): string {
  const enum balancedState {
    BALANCED = "YES",
    UNBALANCED = "NO",
  }

  const stack = new Stack<string>("");

  const brackedPairs: Map<string, string> = new Map([
    ["(", ")"],
    ["{", "}"],
    ["[", "]"],
  ]);

  for (const char of brackets) {
    if (brackedPairs.has(char)) {
      stack.push(char);
    } else {
      if (brackedPairs.get(stack.peek()) !== char) {
        return balancedState.UNBALANCED;
      }

      stack.pop();
    }
  }

  return stack.empty ? balancedState.BALANCED : balancedState.UNBALANCED;
}
