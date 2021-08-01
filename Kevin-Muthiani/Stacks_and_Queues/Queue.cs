using System;

namespace queue {
    public class GolQueue {
        private int[] _items;
        private int _capacity = 0;
        private int _front = 0;
        private int _rear = 0;

        public GolQueue() {
            _items = new int[10];
        }

        public GolQueue(int size) {
            _items = new int[size];
        }

        // Enqueue
        public void Enqueue(int value) {
            if ( _front == 0 && _rear == 0 && _capacity == 0 ) {
                // Queue is empty

                _items[_rear] = value;
                _capacity++;

            } else if ( _capacity == _items.Length ) {
                // Queue is full

                // Create new array
                int length = _items.Length;
                int[] newQueue = new int[length * 2];

                // Copy in cyclic array starting with front item
                for (var i = 0; i < length; i++) {
                	newQueue[i] = _items[_front++];
                    if (_front == length) {
                        _front = 0;
                    }
                }
                _items = newQueue;

                // Push value
                _front = 0;
                _rear = length;
                _items[_rear] = value;
                _capacity++;

            } else if ( _rear == _items.Length -1 ) {
                // Cycle back to first element

                _rear = 0;
                _items[_rear] = value;
                _capacity++;

            } else {

                _items[++_rear] = value;
                _capacity++;

            }
            // Console.Write("Front: " + _front + ", Rear: " + _rear + ", Capacity: " + _capacity + ", Queue: ");
            // Display();
        }

        // Dequeue
        public int Dequeue() {
            int value = -1;

            if ( _capacity == 0 ) {
                // Queue is empty

                Console.WriteLine("Queue is empty");

            } else if ( _front == _rear ) {
                // Queue has only one item

                value = _items[_front];
                // _items[_front] = 0;
                _front = 0;
                _rear = 0;
                _capacity = 0;

            } else if ( _front == _items.Length - 1 ) {
                // Cycle back the front of the queue

                value = _items[_front];
                // _items[_front] = 0;
                _front = 0;
                _capacity--;

            } else {

                value = _items[_front];
                // _items[_front] = 0;
                _front++;
                _capacity--;

            }

            // Console.Write("Front: " + _front + ", Rear: " + _rear + ", Capacity: " + _capacity + ", Queue: ");
            // Display();
            return value;
        }

        // Peek
        public int Peek() {
            int value = -1;

            if ( _capacity == 0 ) {
                Console.WriteLine("Queue is empty");
            } else {
                value = _items[_front];
            }

            return value;
        }

        // Size
        public int Size() {
            return _items.Length;
        }

        // Capacity
        public int Capacity() {
                return _capacity;
        }

        // Display
        public void Display() {

            for (var i = 0; i < _items.Length; i++) {
                Console.Write(_items[i]);
            }
            Console.WriteLine("");
        }


    }

    class Program {
        static void Main (string[] args) {
            GolQueue queue = new GolQueue(3);

            // Tests
            queue.Enqueue(5);
            queue.Enqueue(7);
            queue.Enqueue(3);
            queue.Enqueue(1);
            queue.Dequeue();
            queue.Dequeue();
            queue.Enqueue(4);
            queue.Enqueue(1);
            queue.Dequeue();
            queue.Enqueue(2);
            queue.Enqueue(3);
            queue.Dequeue();
            queue.Dequeue();
            queue.Enqueue(4);
            queue.Enqueue(5);
            queue.Enqueue(6);
            queue.Enqueue(7);
            queue.Enqueue(8);
            queue.Dequeue();

            queue.Display();
            Console.WriteLine(queue.Capacity());
            Console.WriteLine(queue.Peek());
            Console.WriteLine(queue.Size());
        }
    }
}

