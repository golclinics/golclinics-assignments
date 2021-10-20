class MinStack {
  private stack: number[];
  private minValTracker: number[];

  constructor() {
    this.stack = [];
    this.minValTracker = [];
  }
  /**
   * Pushes the element val onto the stack
   *
   * @param val - the value to push onto the stack
   */
  push(val: number): void {
    if (
      this.minValTracker.length === 0 ||
      val <= this.minValTracker[this.minValTracker.length - 1]
    ) {
      this.minValTracker.push(val);
    }

    this.stack.push(val);
  }

  /**
   * Removes the element on top of the stack
   */
  pop(): void {
    if (this.stack.length > 0) {
      if (
        this.minValTracker[this.minValTracker.length - 1] ===
        this.stack[this.stack.length - 1]
      ) {
        this.minValTracker.pop();
      }
      this.stack.pop();
    }
  }

  /**
   * Gets the top element of the stack
   *
   * @returns The top element of the stack
   */
  top(): number {
    return this.stack[this.stack.length - 1];
  }

  /**
   * Retrieves the minimum element in the stack
   *
   * @returns The minimum element in the stack
   */
  getMin(): number {
    return this.minValTracker[this.minValTracker.length - 1];
  }
}
