// Stack Implementation with An array
//
//concrete Examples below
//
//
//Implementing the Push Overflow

//psedocode
// double the stackLength
// create a new Array of double the size
// spread the old array to the new array
// change the pointer of the stacks array to point to the new array
// push the element into the new array

class Stack {
    items = [];
    top = -1;
    constructor(size) {
        this.stackLength = size;
        this.items = new Array(size);
    }

    push = (element) => {
        if (this.stackIsFull()) {
            this.stackLength *= 2;
            let temp = new Array(this.stackLength);
            temp = [...items];
            this.items = temp;
            this.items[++this.top] = element;
        } else {
            this.items[++this.top] = element;
        }
    };

    pop = () => {
        if (this.stackIsEmpty()) throw new Error("Stack is Empty");
        let element = this.items[this.top];
        delete this.items[this.top--];
        return element;
    };

    peek = () => {
        if (this.stackIsEmpty()) throw new Error("Stack is Empty");
        return this.items[this.top];
    };

    stackIsEmpty = () => this.size() - 1 === -1;
    stackIsFull = () => this.top + 1 === this.stackLength;
    size = () => this.top + 1;
}

module.exports = Stack;

// Testing the overflow logic
let stack = new Stack(5);
let { items, push, pop } = stack;

push(4); // element 1
push(6); // element 2
push(7); // element 3
push(4); // element 4
push(6); // element 5

// expects the array to doulbe and push the new element in
push(6); // element 5
push(7);

console.log(stack);

//Discussion. 
//
//Space Complexity for n push operation will be O(n). When the array overflows
//we create a new array by doubling the size of the old array.
//
//Time complexity of Push. Mostly its O(1) but when there is doubling the big
//becomes O(n). But if we consider worst case , it becomes O(n) but this rarely
//happens. (Not sure on this one)
