import { Stack } from "./stack";

export class MyQueue {
  private pushStack: Stack<number>;
  private popStack: Stack<number>;
  private defaultValue = -Infinity;

  constructor() {
    this.pushStack = new Stack<number>(this.defaultValue);
    this.popStack = new Stack<number>(this.defaultValue);
  }
  
  /**
   * Pushes element x to the back of the queue
   *
   * @param x - integer to add to the queue
   */
  push(x: number): void {
    this.pushStack.push(x);
  }

  /**
   * Removes the element from the front of the queue
   *
   * @returns The popped element
   */
  pop(): number {
    let retVal: number = this.defaultValue;

    if (!this.popStack.empty) {
      retVal = this.popStack.peek();
      this.popStack.pop();
    } else {
      while (!this.pushStack.empty) {
        const nextVal = this.pushStack.peek();
        this.pushStack.pop();
        this.popStack.push(nextVal);
      }

      retVal = this.popStack.peek();
      this.popStack.pop();
    }

    return retVal === this.defaultValue ? this.defaultValue : retVal;
  }

  /**
   * Returns the element at the front of the queue
   *
   * @returns The next item waiting to be popped
   */
  peek(): number {
    let retVal: number = this.defaultValue;

    if (!this.popStack.empty) {
      retVal = this.popStack.peek();
    } else {
      while (!this.pushStack.empty) {
        const nextVal = this.pushStack.peek();
        this.pushStack.pop();
        this.popStack.push(nextVal);
      }

      retVal = this.popStack.peek();
    }

    return retVal === this.defaultValue ? this.defaultValue : retVal;
  }

  /**
   * Returns true if the queue is empty, false otherwise
   *
   */
  empty(): boolean {
    return this.popStack.empty && this.pushStack.empty;
  }
}
