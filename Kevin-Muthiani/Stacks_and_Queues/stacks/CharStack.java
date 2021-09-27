package stacks;

import java.util.Arrays;

public class CharStack {
	private static int stackSize = 5;
	private static char[] stack = new char[stackSize];
	private static int top = -1;

	static boolean stackIsFull() {
		return (top == stackSize - 1);
	}

	static boolean stackIsEmpty() {
		return (top == -1);
	}

	public static void pop() {
		if (stackIsEmpty()) {
			System.out.println("Stack Underflow!");
		} else {
			top--;
		}
	}

	public static void push(char value) {
		// Double stack size first if stack is full
		if (stackIsFull()) {
			char[] newStack = Arrays.copyOf(stack, stackSize*2);
			stack = newStack;
			stackSize = stackSize * 2;
		}

		// Push in the value to the top of the stack
		stack[++top] = value;
	}

	public static char peek() {
		if (stackIsEmpty()) {
			System.out.println("Stack is Empty!");
			return '!';
		} else {
			return stack[top];
		}
	}

	public static int capacity() {
		return (top + 1);
	}

	public static void traverse() {
		for (int i=top; i>=0; i--) {
			System.out.print(stack[i]);
		}
		System.out.println("");
	}

	public static void main(String[] args){
		push('e');
		push('a');
		push('i');
		traverse();
		push('d');
		traverse();
		pop();
		pop();
		traverse();
	}
}