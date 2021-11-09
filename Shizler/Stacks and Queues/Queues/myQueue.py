# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:
	
# void push(int x) Pushes element x to the back of the queue.
	
# int pop() Removes the element from the front of the queue and returns it.
	
# int peek() Returns the element at the front of the queue.
	
# boolean empty() Returns true if the queue is empty, false otherwise.
class MyQueue:
    def __init__(self) -> None:
        self.stackInput = []
        self.stackOutput = []
    def push(self,val):
        self.stackInput.append(val)
    def pop(self):
        if not self.stackOutput:
            while self.stackInput:
                self.stackOutput.append(self.stackInput.pop())
        return self.stackOutput.pop()
    def peek(self):
        if not self.stackOutput:
            while self.stackInput:
                self.stackOutput.append(self.stackInput.pop())
        return self.stackOutput[-1]
    def empty(self):
        return not self.stackInput and not self.stackOutput


if __name__ == '__main__':
    que = MyQueue()
    que.push(42)
    print(que.pop()) #42
    que.push(14)
    print(que.empty()) #False
    print(que.peek())  #14
    que.push(28)
    que.push(60)
    print(que.empty()) #False
    print(que.pop()) #14