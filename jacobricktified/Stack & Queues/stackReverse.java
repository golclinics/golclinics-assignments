import java.util.Stack;

// Reverse a String using a Stack
/*
 * Write a program to reverse a string using stack.
 //algorithim:
 Push the character one by one into the Stack of datatype character.
Pop the character one by one from the Stack until the stack becomes empty.
Add a popped element to the character array.
Convert character array to string.
Return reversed string.
 */
class stackReverse{
    public static void main(String[] args){
        String str = "Hello World";
        Stack<Character> stack = new Stack<Character>();
        for(int i=0;i<str.length();i++){
            stack.push(str.charAt(i));
        }
        StringBuffer sb = new StringBuffer();
        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }
        System.out.println(sb.toString());
    }

}