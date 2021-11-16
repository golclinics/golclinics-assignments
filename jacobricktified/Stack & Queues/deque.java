
//Implement a deque
class Deque {
    private int[] arr;
    private int size;
    private int front;
    private int rear;
    public Deque(int capacity) {
        arr = new int[capacity];
        size = 0;
        front = 0;
        rear = -1;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public boolean isFull() {
        return size == arr.length;
    }
    public int size() {
        return size;
    }
    public void addFront(int item) {
        if (isFull()) {
            throw new RuntimeException("Queue is full");
        }
        if (rear == -1) {
            rear = 0;
        }
        arr[front] = item;
        front = (front + 1) % arr.length;
        size++;
    }
    public void addRear(int item) {
        if (isFull()) {
            throw new RuntimeException("Queue is full");
        }
        if (rear == -1) {
            rear = 0;
        }
        rear = (rear + 1) % arr.length;
        arr[rear] = item;
        size++;
    }
    public int removeFront() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int item = arr[front];
        front = (front + 1) % arr.length;
        size--;
        if (size == 0) {
            front = 0;
            rear = -1;
        }
        return item;
    }
    public int removeRear() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int item = arr[rear];
        rear = (rear - 1 + arr.length) % arr.length;
        size--;
        if (size == 0) {
            front = 0;
            rear = -1;
        }
        return item;
    }
    public int peekFront() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return arr[front];
    }
    public int peekRear() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        return arr[rear];
    }
}
