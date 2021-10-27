export class Stack<T> {
  private elements: T[];
  private defaultValue: T;

  constructor(defaultVal: T) {
    this.elements = [];
    this.defaultValue = defaultVal;
  }

  private get lastIdx(): number {
    if (this.size === 0) return 0;
    return this.size - 1;
  }

  /**
   * Returns boolean representing if the stack is empty or not
   *
   * @returns boolean representing if size is equal to zero
   */
  get empty(): boolean {
    return this.size === 0;
  }

  /**
   * Returns the size of the elements array
   *
   * @returns integer representing size of the elements array
   */
  get size(): number {
    return this.elements.length;
  }

  /**
   * Returns the last added element without removing it from the stack.
   *
   * @returns the last added element
   */
  peek(): T {
    if (this.empty) {
      return this.defaultValue;
    }

    return this.elements[this.lastIdx];
  }

  /**
   * Pushes the element x onto the stack
   *
   * @param x - The next element to add to the stack
   */
  push(x: T): void {
    this.elements.push(x);
  }

  /**
   * Removes the top element of the stack
   *
   */
  pop(): void {
    if (this.size > 0) this.elements.pop();
  }
}
