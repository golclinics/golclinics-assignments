//Implement a stack in a language of your choice using a Tuple of size 2
public class stacksTuple {
    public static void main(String[] args) {
        // Create a stack of size 3
        Stack<Tuple<Integer, Integer>> s3 = new Stack<Tuple<Integer, Integer>>(3);
        // Push 2 elements into stack s3
        s3.push(new Tuple<Integer, Integer>(1, 2));
        s3.push(new Tuple<Integer, Integer>(3, 4));
        // Print and display top element of stack s3
        System.out.println("top element of s3:\n" + s3.top());
        // Print and display stack s3
        System.out.println("\ns3 after pushing 2 elements :\n" + s3);
        // Pop element from stack s3
        s3.pop();
        // Print and display stack s3
        System.out.println("\ns3 after popping 1 element :\n" + s3);
    }
    
}
