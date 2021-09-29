package gol;

/**
 *
 * @author leesangoroh
 */
public class MinimumSwaps {
    
    static int minimumSwaps (int [] array) {
        
        int count=0;
        int temp;
        int length = array.length -1;
        
        for (int i = 0; i<length; i++) {
            
            //if (array[i] < array[i++] || array[i] == array[i++]) {
               
              //  continue;
            //}
            
            if (array[i]>array[i++]) {
                temp = array[i];
                array[i] = array[i++];
                array[i++] = temp;
                
                count++;
            }
        }
        
        return count;
    }
    
    
    public static void main (String [] args) {
        
        int [] arr = {5,7,1,3,0,8,6};
        
        System.out.println(minimumSwaps(arr));
    }
}
