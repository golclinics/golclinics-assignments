import java.util.Stack;
/**
 Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
	
	 
	
	Implement the MinStack class:
	
	 
	
	MinStack() initializes the stack object.
	void push(int val) pushes the element val onto the stack.
	void pop() removes the element on the top of the stack.
	int top() gets the top element of the stack.
	int getMin() retrieves the minimum element in the stack.
	 
	
	 
	
	Example:
	
	
	Input
	["MinStack","push","push","push","getMin","pop","top","getMin"]
	[[],[-2],[0],[-3],[],[],[],[]]
	
	 
	
	Output
	[null,null,null,null,-3,null,0,-2]                                                                                                                                                  
 */
//implement two stacks peek the min value of integers
public class MinStack {
    Stack<Integer> stack;
    Stack<Integer> minStack;
    /** initialize your data structure here. */
    public MinStack() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }
    
    public void push(int x) {
        stack.push(x);
        if(minStack.isEmpty() || x <= minStack.peek()){
            minStack.push(x);
        }
    }
    
    public void pop() {
        if(stack.peek() == minStack.peek()){
            minStack.pop();
        }
        stack.pop();
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
    //main method
    public static void main(String[] args) {
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-1);
        System.out.println(minStack.getMin());
        minStack.pop();
        System.out.println(minStack.top());
        System.out.println(minStack.getMin());
    }

    

    
}
