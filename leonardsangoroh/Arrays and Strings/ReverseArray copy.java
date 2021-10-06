package gol;

/*
 @author leesangoroh
 */

//Importing java class
import java.util.Arrays;


public class ReverseArray {
    
    /* Write a function reverseArray(A) that takes in an array A and reverses it,
    without using another array or collection data structure; in-place.*/

    static void ReverseArray(int [] A) {
        
        int length = A.length - 1;
        
        //Checking if the array is reversible
        if ( A == null || A.length <= 1) {
            System.out.println("Invalid output");
        }
        
        int endIndex = A.length -1;
        
        //Swapping
        for (int i = 0; i< A.length/2; i++) {
            
            int  tempVar = A[i];
            A[i] = A[endIndex];
            A[endIndex] = tempVar;
            
            endIndex--;
        }
        
        //Printing the reversed array
        System.out.println(Arrays.toString(A));
        
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        
        int [] array = { 1,4,5,7};
        
        ReverseArray(array);
    }
    
}
