// Implement a minstack - ability to get a minimum value in the stack 

//  [1, 2, 3, 1, 2]

class Stack {
    constructor() {
      this.stack = [];
      this.size = 10;
      this.capacity = 0;
      this.minStack = [];
    }

    // Push
    push(val){
      //  Check if array is full
      if(this.capacity === this.size) {
        console.log('stack is full');
        return
      }

      this.stack.push(val);
      this.capacity++;

      //update minStack
      if(this.minStack.length == 0 || val <= this.getMinValue()) {
        this.minStack.push(val);
      }
    }

    // Pop
    pop() {
      if(this.capacity == 0) {
        console.log('stack is empty');
        return
      }

      let removed =  this.stack.pop();
      let minValue = this.getMinValue();
      if (removed == minValue) {
        this.minStack.pop()
      }

      this.capacity--;

      return removed;
    }

    traverse() {
      console.log("Stack: ", this.stack);
    }

    // For debugging
    traversemin() {
      console.log("minStack: ", this.minStack);
    }

    // Min Value
    getMinValue() {
      // Peek last item of minStack
      return this.minStack[this.minStack.length - 1];
    }
  }

  // Tests
  let stack = new Stack;


  console.log('Pushing...');

  stack.push(1);
  stack.traverse()
  stack.traversemin()

  stack.push(2);
  stack.traverse()
  stack.traversemin()

  stack.push(3);
  stack.traverse()
  stack.traversemin()

  stack.push(1);
  stack.traverse()
  stack.traversemin()

  stack.push(2);
  stack.traverse()
  stack.traversemin()

  console.log('');
  console.log('Popping...');

  stack.traverse()
  stack.traversemin()
  console.log("Min: ",stack.getMinValue());

  stack.pop()
  stack.traverse()
  stack.traversemin()
  console.log("Min: ",stack.getMinValue());

  stack.pop()
  stack.traverse()
  stack.traversemin()
  console.log("Min: ",stack.getMinValue());

  stack.pop()
  stack.traverse()
  stack.traversemin()
  console.log("Min: ",stack.getMinValue());