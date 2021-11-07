
import java.util.ArrayList;
import java.util.Stack;
public class MinStack {
    public static void main(String[] args) {
        ArrayList<Integer> nums = new ArrayList<>();

        nums.add(5);
        nums.add(2);
        nums.add(8);
        nums.add(1);
        nums.add(3);
        nums.add(-5);

        minStack(nums);
    }

    public static int minStack(ArrayList<Integer> nums){
        Stack<Integer> allNumbers = new Stack();
        Stack<Integer> minNumbers = new Stack();

        int n = nums.size() - 1;
        int initialMin  = nums.get(0);
        minNumbers.push(initialMin);

        for(int i = 0; i <= n; i++){
            allNumbers.push(nums.get(i));
            if(nums.get(i) < minNumbers.peek()){
                minNumbers.push(nums.get(i));
            }else if(nums == null){
                System.out.println("There are no minimum values, the stack is empty.");
            }
        }
        System.out.println("Peek number is: " + minNumbers.peek());
        return minNumbers.peek();
    }

}