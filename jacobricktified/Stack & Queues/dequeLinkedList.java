import org.w3c.dom.Node;

// Implement a queue in a language of your choice using a linked list
public class dequeLinkedList {
    private Node head;
    private Node tail;
    private int size;
    public dequeLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }
    public boolean isEmpty() {
        return size == 0;
    }
    public boolean isFull() {
        return false;
    }
    public int size() {
        return size;
    }
    public void addFront(int item) {
        Node newNode = new Node(item);
        if (isEmpty()) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
        size++;
    }
    public void addRear(int item) {
        Node newNode = new Node(item);
        if (isEmpty()) {
            head = newNode;
            tail = newNode;
        } else {
            tail.next = newNode;
            tail = newNode;
        }
        size++;
    }
    public int removeFront() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int item = head.item;
        head = head.next;
        size--;
        if (size == 0) {
            head = null;
            tail = null;
        }
        return item;
    }
    public int removeRear() {
        if (isEmpty()) {
            throw new RuntimeException("Queue is empty");
        }
        int item = tail.item;
        if (size == 1) {
    
}
