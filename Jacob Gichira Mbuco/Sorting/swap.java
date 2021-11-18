//Assignment two: How do you swap to numbers (Implement a function to swap two numbers_
//wrong answer
//after swap a is supposed to be 20 and b is supposed to be 10

public class swap {
    public static void main(String[] args) {
        int a = 10;
        int b = 20;
        System.out.println("Before swap a is " + a + " and b is " + b);
        swap(a, b);
        System.out.println("After swap a is " + a + " and b is " + b);
    }

    public static void swap(int a, int b) {
        int temp = a;
        a = b;
        b = temp;
    }
    

    
    
}
//insertion sort is a sorting algorithm that works by taking an element from the array and inserting it into the sorted portion of the array.
