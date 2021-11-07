public class MyQueue {
    private static int[] randomQueue = new int[0];
    private static int front, back,size = 0;

    public MyQueue(int Size){
        randomQueue = new int[Size];
    }

    public void push(int element){
        if(randomQueue.length > size){
            randomQueue[back] = element;
            ++back;
            ++size;
        }else{
            System.out.println("The queue is full! Wait for a dequeue.");
        }
    }

    public int pop(){
        int frontValue = 0;
        if(front == back){
            frontValue = -1;
        }else{
            frontValue = randomQueue[front];

        }


        for(int i = 0; i < size; i++){
            if(i < size -1 && back >= 1) {
                randomQueue[i] = randomQueue[i + 1];
            }
        }
        randomQueue[size - 1] = 0;
        --size;
        --back;

        return frontValue;
    }

    public int peek(){
        return randomQueue[front];
    }

    public boolean empty(){
        return size == 0;
    }

    public static void main(String[] args) {
        MyQueue athletes = new MyQueue(5);
        athletes.push(1);
        athletes.push(2);
        athletes.push(5);
        athletes.push(4);
        athletes.push(3);

        athletes.pop();
        athletes.pop();
        athletes.pop();


        athletes.push(7);



        for(int element:MyQueue.randomQueue){
            System.out.println(element);
        }

        System.out.println("The peek is: "+athletes.peek());
        System.out.println("Is array empty: "+ athletes.empty());

    }


}
