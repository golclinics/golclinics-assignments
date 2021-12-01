/*
Given a balanced parentheses string s, return the score of the string.
	
	 
	
	The score of a balanced parentheses string is based on the following rule:
	
	 
	
	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.
	 
	
	 
	
	Examples:
	
	
	Input: s = "()"
	Output: 1
	
	 
	
	Input: s = "(())"
	Output: 2
	
	 
	
	Input: s = "()()"
	Output: 2
	
	 
	
	Input: s = "(()(()))"
	Output: 6
*/
public class parenthesesScore {
    public int scoreOfParentheses(String S) {
        int score = 0;
        int level = 0;
        for(int i = 0; i < S.length(); i++){
            if(S.charAt(i) == '('){
                level++;
            }else{
                level--;
            }
            if(S.charAt(i) == '(' && S.charAt(i+1) == ')'){
                score += 1 << level;
            }
        }
        return score;
    }
    //main method for testing
    public static void main(String[] args){
        parenthesesScore test = new parenthesesScore();
        System.out.println(test.scoreOfParentheses("(()(()))"));
    }
    
}
