public class MyStack {

    private static int[] myStack = new int[0];
    private static int rear= 0;
    private static int size = 0;

    public MyStack(int Size){
        myStack = new int[Size];
    }

    public void push(int x){
        if(size < myStack.length){
            myStack[rear] = x;
            ++rear;
            ++size;


        }else{
            System.out.println("The stack is full");
        }
    }

    public int pop(){
        int lastIn = myStack[rear -1];
        if(rear - 1 == 0){
            throw new IllegalArgumentException("The stack is empty!");
        }

        myStack[size -1] = 0;
        --rear;
        --size;

        System.out.println("Last in is: "+lastIn);
        return lastIn;
    }

    public boolean empty(){
        return size == 0;
    }

    public int top(){
        return myStack[rear - 1];
    }
    public static void main(String[] args) {
        MyStack numbers = new MyStack(5);
        numbers.push(6);
        numbers.push(7);
        numbers.push(3);

        numbers.pop();

        System.out.println("Top is: " + numbers.top());

        for(int element: MyStack.myStack){
            System.out.println(element);
        }
    }
}
