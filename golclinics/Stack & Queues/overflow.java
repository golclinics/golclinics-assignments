import java.util.Stack;

/*
As follow-up to the stack operations discussed in lesson 1, implement the overflow logic (extension of an array when pushing an element to a full stack)
*/
public class overflow {
    public static void main(String[] args) {

        // Create a stack of size 5
        Stack<Integer> stack = new Stack<Integer>();
        // Push elements to stack
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        // Check if stack is full
        if (((Object) stack).isFull()) {
            System.out.println("Stack is full");
        }
        // Push element to stack
        stack.push(6);
        // Check if stack is full
        if (((Object) stack).isFull()) {
            System.out.println("Stack is full");
        }
        // Pop elements from stack
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        System.out.println(stack.pop());
        // Check if stack is empty
        if (stack.isEmpty()) {
            System.out.println("Stack is empty");
        }


    }


        
       
       
    
}
 
