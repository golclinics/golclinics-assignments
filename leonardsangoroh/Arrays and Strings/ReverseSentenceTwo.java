package gol;

/**
 *
 * @author leesangoroh
 */

import java.util.Arrays;


public class ReverseSentenceTwo {


    private static void reverseSentence(char[] array) {
        var start = 0;
        for(var end=0; end<array.length; end++) {
            if(array[end]== ' ') {
                System.out.println(Arrays.toString(array));
                reverse(array, start, end);
                System.out.println(Arrays.toString(array));
                start = end + 1;
            }
        }
        System.out.println(Arrays.toString(array));

        // Reverse the entire String
        reverse(array, 0, array.length - 1);
        System.out.println(Arrays.toString(array));


        System.out.println("Reversed array : ");
        System.out.println(Arrays.toString(array));
    }

    private static void reverse(char[] array, int start, int end) {
        char temp;
            while (start <= end) {
                // Swapping the first and last character
                temp = array[start];
                array[start] = array[end];
                array[end] = temp;
                start++;
                end--;
            }
    }
    
  
        
    public static void main(String[] args) {
        char[] a = { 't', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd', ' ' };
        reverseSentence(a);
    }
}
