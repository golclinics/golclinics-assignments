class Stack:
    """
    The aim is to implement a Stack class that has the following behaviors:

    push(takes in an element to add to a stack as an argument)- adds an item to the top of the stack
    pop(takes no argument) - removes an item from the top of the stack (and returns the value of that item)
    size() - returns the size of the stack
    peek() - returns the value of the item at the top of stack (without removing that item)
    is_empty() - returns True if the stack is empty and False otherwise
    capacity() - returns the number of elements in the stack
    """
    def __init__(self, initial_size):
        self.arr = [0 for _ in range(initial_size)]
        self.top = -1
        self.num_of_elements = 0

    def push(self, value):
        if self.top + 1 == len(self.arr):
            print("stack overflow, adding some space for extra element(s)")
            self.handle_full_capacity()
        self.top += 1
        self.arr[self.top] = value
        self.num_of_elements += 1

    def handle_full_capacity(self):
        old_arr = self.arr
        self.arr = [0 for _ in range(len(old_arr) * 2)]
        for index, element in enumerate(old_arr):
            self.arr[index] = element

    def pop(self):
        if self.is_empty():
            print("stack undeflow")
            self.top = -1
            return None
        self.num_of_elements -= 1
        return self.arr[self.num_of_elements]
        self.top = self.top - 1

    def is_empty(self):
        return self.num_of_elements == 0

    def capacity(self):
        return self.top + 1

    def size(self):
        return len(self.arr)

    def peek(self):
        return self.arr[self.top]

if __name__ == '__main__':
    # creating an object
    s = Stack(10)

    # pushing elements to the stack - more than its initialized capacity
    for num in range(100):
        s.push(num)
    print(s.arr)



    
    
