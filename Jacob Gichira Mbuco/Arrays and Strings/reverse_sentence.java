/*1. we will use the two pointer approach
2. we will reverse all the characters in  a word
3. we will reverse until the string end
4. return the reversed array */
import java.util.*;
public class reverse_sentence(char []A){
    int i=0; int j = A.length-1;
    while (i<j){
        char temp = A[i];
        A[i]= A [j];
        A[j]= temp;
        i++; 
        j--;
    }
     

}