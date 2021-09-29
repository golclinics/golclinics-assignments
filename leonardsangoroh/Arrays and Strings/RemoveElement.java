package gol;

import java.util.List;
import java.util.stream.IntStream;
import java.util.Arrays;
import java.util.stream.Collectors;

/**
 *
 * @author leesangoroh
 */
public class RemoveElement {
    
    static void removeElement (int[] nums, int val) {
        
        int length = nums.length - 1;
        
        List<Integer> arrayList = IntStream.of(nums).boxed().collect(Collectors.toList());
         
        for (int i = 0; i< length; i++) {
            
            if (nums[i] == val) {

                arrayList.remove(i);
            
            }
        }
        
        int [] newArr = arrayList.stream().mapToInt(Integer::intValue).toArray();
        
        int newLength = newArr.length-1;
        int count = 0;
        
        for (int j=0; j<= newLength; j++) {
            count++;
        }
        
        System.out.println(count);
        
        System.out.println(Arrays.toString(newArr));
        
    }
    
    public static void main (String [] args) {
        
        int [] arr = {4,2,7,5,6,3,2,1,8};
        
        int value = 4;
        
        removeElement(arr,value);
        
        
        
        
    }
}
