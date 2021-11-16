import java.util.Scanner;
import java.util.Stack;
public class ReverseString {
 
    public static void main(String[] args) {
 
          //Take input string
          Scanner in = new Scanner(System.in);
          System.out.println("Enter a string");
 
          String str = in.nextLine();
 
          //Declare a stack
          Stack stack = new Stack<>();
 
          /**
           * Traverse a string and push each character
           * of a string in a stack.
           */
          for(int i = 0; i < str.length(); i++) {
               stack.push(str.charAt(i));
          }
 
          System.out.println("Reverse of a string");
 
         //When stack is not empty, pop each character
          while(!stack.empty()) {
              System.out.print(stack.pop());
          }
      }
}