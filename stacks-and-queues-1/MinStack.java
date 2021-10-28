import java.util.*;

public class MinStack {
    Stack<Integer> numbers;
    Integer minValueTracker;

    MinStack() {
        numbers = new Stack<>();
    }

    void getMin(){
        if (numbers.isEmpty()){
            System.out.println("Stack is empty");
        } else {
            System.out.println("Min element is: " + minValueTracker);
        }
    }

    void push(Integer integer){
        if (numbers.isEmpty()){
            minValueTracker = integer;
            numbers.push(integer);
            return;
        }

        if (integer < minValueTracker){
            numbers.push((integer * 2) - minValueTracker);
            minValueTracker = integer;
        } else {
            numbers.push(integer);
            System.out.println("Number inserted");
        }
    }

    void pop(){
        if (numbers.isEmpty()){
            System.out.println("Stack is empty");
            return;
        }

        System.out.println("Removed top element");
        Integer top = numbers.pop();

        if (top < minValueTracker){
            System.out.println(minValueTracker);
            minValueTracker = (minValueTracker * 2) - top;
        } else {
            System.out.println(top);
        }
    }

    Integer top(){
        if (!(this.numbers.size() == 0)){
            return this.minValueTracker;
        }
        return minValueTracker;
    }
}