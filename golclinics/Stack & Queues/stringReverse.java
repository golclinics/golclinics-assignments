import java.util.Stack;

//Write a program that reads a String and reverses the String using Stack Push and Pop operations
public class stringReverse {
    public static void main(String[] args) {
        Stack<Character> stack = new Stack<Character>();
        String str = "Hello World";
        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        while (!stack.isEmpty()) {
            sb.append(stack.pop());
        }
        System.out.println(sb.toString());
    }
    
}
