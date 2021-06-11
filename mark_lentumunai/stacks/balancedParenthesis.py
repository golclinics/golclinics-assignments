class stack:
    def __init__(self):
        self.arr = []
        self.top = -1
    def push(self, element):
        self.top += 1
        self.arr.append(element)
    def pop(self):
        self.arr.pop()

    def get_capacity(self):
        return len(self.arr)

    def get_peek(self):
        return self.arr[top]

def are_pairs(par1, par2):
    #the above methods takes in a pair of parenthesis then checks if their balanced using equality operator
    # returns a boolean for every equality check
    # True if balanced and False if not balanced
    if par1 =="{" and par2 == "}":
        return True
    else:
        return False
    if par1 == "(" and par2 == ")":
        return True
    else:
        return False
    if par1 == "[" and par2 == "]":
        return True
    else:
        return False
def balancedParenthesis(parenthesis):
    st = stack()
    #checks if parenthesis is empty
    if len(parenthesis) == 0:
        return True
    else:
        for track in range(len(parenthesis)):
            if parenthesis[track] == "(" or parenthesis[track] == "{" or parenthesis[track]  == "[":
                st.push(parenthesis[track])
            else:
                if parenthesis[track] == ")" or parenthesis[track] == "}" or parenthesis[track]  == "]":
                    if are_pairs(parenthesis[-1], parenthesis[track]) or len(st.arr) != 0:
                        st.pop()
                    else:
                        return False
                        
        if st.get_capacity() == 0:
            return True
        else:
            return False

if __name__ == "__main__":
    print("balanced parenthesis" if balancedParenthesis('[{()}]') else "unbalanced parenthesis")
    print("balanced parenthesis" if balancedParenthesis('((3^2 + 8)*(5/2))/(2+6)') else "unbalanced parenthesis")


