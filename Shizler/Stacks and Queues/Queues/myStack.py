# Q2: Implement Stack using Queues

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:
	
# void push(int x) Pushes element x to the top of the stack.
	
# int pop() Removes the element on the top of the stack and returns it.
	
# int top() Returns the element on the top of the stack.
	
# boolean empty() Returns true if the stack is empty, false otherwise.
class MyStack:
    def __init__(self) -> None:
        self.queueInput = []
        self.queueOutput = []
        self.top_elem = 0
    def push(self,val):
        self.queueInput.append(val)
        self.top_elem = val
        print(self.queueInput)
    def pop(self):
        i = len(self.queueInput)
        while i > 1:
            self.queueOutput.append(self.queueInput.pop(0))
            i-=1
        self.top_elem = self.queueInput.pop()

        self.queueInput, self.queueOutput = self.queueOutput, self.queueInput

        return self.top_elem
    def top(self):
        return self.queueInput[-1]
    def empty(self):
        return not self.queueOutput


if __name__ == '__main__':
    st = MyStack()
    st.push(1)
    st.push(2)
    st.push(3)
    print(st.top())
    print(st.pop())
    print(st.top())
    print(st.empty())
