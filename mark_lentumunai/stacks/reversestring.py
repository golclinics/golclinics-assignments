class stack:
    """
    implementing a stack class
    """
    def __init__(self):
        self.arr = []
    def push(self, element):
            self.arr.append(element)
    def pop(self):
        return self.arr.pop()

def reverse(string):
    #this function creates a stack objects that uses the push() and pop() method to reverse string
    s1 = stack()
    empty_string = "" 
    for letter in string:
        s1.push(letter)
    while len(s1.arr) != 0:
        empty_string += s1.pop()
    return empty_string
if __name__ == '__main__':

    s = stack()
    #calling on the function reverse and passing the string you want it to reverse
    print(reverse("hey"))

    
            