import java.util.ArrayList;
import java.util.*;

public class BalancedParenthesis {
    int parenthesisScore(String string){
        int score = 0;
        Stack<Integer>scores =  new Stack<>();

        for (int i = 0; i < string.length(); i++){
            if (string[i] == '('){
                scores.push(score);
                score = 0;
            } else {
                score = scores.pop() + Math.round((score * 2));            }
        }

        return score;
    }
}
