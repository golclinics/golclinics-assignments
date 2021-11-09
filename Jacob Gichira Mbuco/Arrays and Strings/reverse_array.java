import java.util.*;
public class reverse_array {
     public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of elements in the array");
        int n = input.nextInt();
        int[] arr = new int[n];
        System.out.println("Enter the elements of the array");
        for(int i = 0; i < n; i++) {
            arr[i] = input.nextInt();
        }
        for(int i = n-1; i >= 0; i--) {
            System.out.print(arr[i] + " ");
        }
    }
}
// time complexity: O(n)
// space complexity: O(1)
   /*
    static void  rvereseArray(
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


       */