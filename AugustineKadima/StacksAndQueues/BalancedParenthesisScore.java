
import java.util.Stack;

public class BalancedParentesisScore{
    private static Stack<Character> bracePairs = new Stack();
    private static int Score = 0;
    public static void main(String[] args) {
        String parenthesis = "(())[]";
        findScore(parenthesis);
    }

    public static int findScore(String braces){

        int n = braces.length() -1;

        for(int i = 0; i <= n; i++){
            char currentCharacter =braces.charAt(i);
            if(currentCharacter == '(' || currentCharacter == '[' || currentCharacter == '{'){
                bracePairs.push(currentCharacter);
            }else if(currentCharacter == '}' && bracePairs.peek() == '{'){
                Score++;
                bracePairs.pop();
            }else if(currentCharacter == ')' && bracePairs.peek() == '('){
                Score++;
                bracePairs.pop();
            }else if(currentCharacter == ']' && bracePairs.peek() == '['){
                Score++;
                bracePairs.pop();
            }else if(bracePairs == null){
                return 0;
            }else{
                System.out.println("The string is not balanced");
            }
        }
        System.out.println("Score is: " +Score);
        return Score;
    }

}