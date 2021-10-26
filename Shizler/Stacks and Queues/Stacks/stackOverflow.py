class stackOverflow():
    def __init__(self,size):
        self.size = size
        self.top = 0
        self.stack = [0]*self.size

    def push(self,val):
        if(self.top > len(self.stack)-1):
            print("Stack overflow")
            # extend the array and push()
            self.stack = self.stack + ([0]*len(self.stack))
            self.stack[self.top] = val
            self.top+=1
        else:
            self.stack[self.top] = val
            self.top+=1
        
        return self.stack

if __name__ == '__main__':
    st = stackOverflow(3)
    print(st.push(1))
    print(st.push(2))
    print(st.push(3))
    print(st.push(4))