
import java.util.*;
//Write a function reverseSentence(A) that takes in an array of characters, A, and reverses the the "words" (not individual characters).
/*Example:

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A)
A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
*/
public class reverse_sentence {
    public void reverseSentence(char[] A) {
        int i = 0;
        int j = A.length - 1;
        while (i < j) {
            char temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            i++;
            j--;
        }
    }
}
// time complexity: O(n)
// space complexity: O(1)