import { MyQueue as Queue } from "./queue-using-stacks";

class MyStack {
  private pushQueue: Queue;
  private helperQueue: Queue;
  private defaultValue = -Infinity;

  constructor() {
    this.pushQueue = new Queue();
    this.helperQueue = new Queue();
  }

  /**
   * Pushes element x to the top of the stack
   *
   * @param x - Integer to push onto the stack
   */
  push(x: number): void {
    this.pushQueue.push(x);
  }

  /**
   * Removes the element on the top of the stack and returns it
   *
   * @returns The element just popped from the stack
   */
  pop(): number {
		let lastQueueItem = this.drainPushQueue();

    this.drainHelperQueue();

    return lastQueueItem === this.defaultValue
      ? this.defaultValue
      : lastQueueItem;
  }

  /**
   * Returns the element on the top of the stack
   *
   * @returns The integer on top of the stack
   */
  top(): number {
		let lastQueueItem = this.drainPushQueue();

    this.drainHelperQueue();

    if (lastQueueItem !== this.defaultValue) {
      this.push(lastQueueItem);
    }

    return lastQueueItem === this.defaultValue
      ? this.defaultValue
      : lastQueueItem;
  }

  /**
   * Returns true if the stack is empty, false otherwise
   *
   * @returns Boolean indicating whether the stack is empty or not
   */
  empty(): boolean {
    return this.pushQueue.empty() && this.helperQueue.empty();
  }

  /**
   * Drain the helperQueue elements back into the pushQueue
   */
  private drainHelperQueue(): void {
    while (!this.helperQueue.empty()) {
      this.pushQueue.push(this.helperQueue.pop());
    }
  }

  /**
   * Drain the pushqueue elements into the helperQueue
   */
  private drainPushQueue(): number {
    let lastQueueItem = this.defaultValue;

    while (!this.pushQueue.empty()) {
      if (lastQueueItem !== this.defaultValue) {
        this.helperQueue.push(lastQueueItem);
      }

      lastQueueItem = this.pushQueue.pop();
    }

    return lastQueueItem;
  }
}
