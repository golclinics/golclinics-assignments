# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
class MinStack:
    def minStack(self):
        global stack, min_stack
        stack = []
        min_stack = []
        print(stack)
    def push(self,a):
        if len(min_stack) == 0 or a < min_stack[-1]:
            min_stack.append(a)
        stack.append(a)
        print(stack)
    def pop(self):
        if stack[-1] == min_stack[-1]:
            min_stack.pop()
        stack.pop()
        print(stack)
    def top(self):
        if len(stack) > 0:
            print(stack[-1])
    def getMin(self):
        val = min_stack[-1]
        print(val)
    # Input
    # ["MinStack","push","push","push","getMin","pop","top","getMin"]
    # [[],[-2],[0],[-3],[],[],[],[]]
if __name__ == '__main__':
    s1 = MinStack()
    s1.minStack()
    s1.push(-2)
    s1.push(0)
    s1.push(-3)
    s1.getMin()
    s1.pop()
    s1.top()
    s1.getMin()



