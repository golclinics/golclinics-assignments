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

/**
 * A Stack with overflow logic implemented
 */
class OverFlow {
  private nums: number[];
  private defaultValue = Infinity;
  private top = 0;

  constructor(initialSize = 5) {
    this.nums = new Array(initialSize).fill(this.defaultValue);
  }

  private stackIsFull() {
    return this.top >= this.nums.length;
  }

  get size() {
    return this.nums.length;
  }

  push(val: number): void {
    if (this.stackIsFull()) {
      console.log("Stack overflow");

      const prevValues = [...this.nums];

      // reduce stack overflows by squaring the size of full stack
      const newArr = new Array(
        this.size === 1 ? this.size * 2 : this.size ** 2
      ).fill(this.defaultValue);

      this.nums = [...prevValues, ...newArr];
    }

    this.nums[this.top++] = val;
  }
}
