

import java.util.Arrays;

public class StackByArray {
	private static int stackSize = 5;
	private static int[] stack = new int[stackSize];
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

	public static void push(int value) {
		// Double stck size first if stack is full
		if (stackIsFull()) {
			// int[] newStack = new int[stackSize*2];
			// for (var i = 0; i < stackSize; i++) {
			// 	newStack[i] = stack[i];
			// }

			// Using in-built Arrays.copyOf()
			int[] newStack = Arrays.copyOf(stack, stackSize*2);

			stack = newStack;
			stackSize = stackSize * 2;

		}
		// Push in the value to the top of the stack
		stack[++top] = value;
	}

	public static void peek() {
		if (stackIsEmpty()) {
			System.out.println("Stack is Empty!");
		} else {
			System.out.println(stack[top]);
		}
	}

	public static int capacity() {
		return (top + 1);
	}

	public static void traverse() {
		// for (var i=0; i<=top; i++) {
		for (int i=top; i>=0; i--) {
			System.out.print(stack[i]);
		}
		System.out.println("");
	}

	public static void main(String[] args){
		// Testing
		push(5);
		push(1);
		push(3);
		push(2);
		push(4);
		traverse();
		System.out.println(capacity());
		push(9);
		traverse();
		System.out.println(capacity());
		push(4);
		traverse();
		System.out.println(capacity());
		pop();
		traverse();
		System.out.println(capacity());
		pop();
		traverse();
		System.out.println(capacity());
		pop();
		traverse();
		System.out.println(capacity());
		pop();
		traverse();
		System.out.println(capacity());
		push(7);
		traverse();
	}
}