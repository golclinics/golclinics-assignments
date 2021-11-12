/*Creating a deep copy of an array, write a function deepCopy
that takes an array of any type and returns a new array with the same elements.*/
public class main{
    public static int[] deepCopy(){// in this line
        int[] arr = {1,2,3,4,5};
        int[] arr2 = new int[arr.length];
        for(int i = 0; i < arr.length; i++){
            arr2[i] = arr[i];
        }
        return arr2;
    }
}