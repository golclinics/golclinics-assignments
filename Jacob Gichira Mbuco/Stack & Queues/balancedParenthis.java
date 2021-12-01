import java.util.Stack;

//given different parenthis as string of charcters determine if they are balaced
//use stack
public class balancedParenthis {
    public static void main(String[] args) {
        String str = "({[]})";
        System.out.println(isBalanced(str));
    }
    public static boolean isBalanced(String str) {
        Stack<Character> stack = new Stack<Character>();
        for(int i = 0; i < str.length(); i++) {
            char c = str.charAt(i);
            if(c == '(' || c == '{' || c == '[') {
                stack.push(c);
            }
            else if(c == ')' || c == '}' || c == ']') {
                if(stack.isEmpty()) {
                    return false;
                }
                char top = stack.pop();
                if(!((top == '(' && c == ')') || (top == '{' && c == '}') || (top == '[' && c == ']'))) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
    
}
