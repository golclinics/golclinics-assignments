import java.util.*;
public class reverse_array {
     
   
    static void rvereseArray(
                    int start, int end)
    {
      
        int temp;
        int arr [] = {1,2,3,4,5};
          
        while (start < end)
        {
            temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
            
        }
      System.out.println(arr);
    }
}


       