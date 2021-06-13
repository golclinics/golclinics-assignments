#number 2
"""
Write a program that reads a String 
and reverses the String using Stack Push and Pop operations
"""
def reverse(s):
    stack = []
    temp = ""
    for i in range(len(s)):
        if s[i] == ' ':
            stack.append(temp)
            temp = ""
        else:
            temp = temp + s[i]
    stack.append(temp)
    while len(stack) != 0:
        temp = stack[len(stack) - 1]
        print(temp, end = " ")
        stack.pop()
            
    print()

s = "Stacks assignment string reverse"
reverse(s)

#number 3
"""
A bracket is considered to be any one of the following characters: (, ), {, }, [, or ]. Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: [], {}, and ().

A matching pair of brackets is not balanced if the set of brackets it encloses are not matched. For example, {[(])} is not balanced because the contents in between { and } are not balanced. The pair of square brackets encloses a single, unbalanced opening bracket, (, and the pair of parentheses encloses a single, unbalanced closing square bracket, ].

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

It contains no unmatched brackets.
The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
Given strings of brackets, write a function that determines whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.
"""
def check():
    stack = []
    s = input()
    for c in s:
        #print(c)
        if c == '(':
            stack.append(0);
        elif c == ')':
            if len(stack) > 0 and stack[-1] == 0:
                stack.pop()
            else:
                return -1
        elif c == '[':
            stack.append(2)
        elif c == ']':
            if len(stack) > 0 and stack[-1] == 2:
                stack.pop()
            else:
                return -1
        if c == '{':
            stack.append(4)
        elif c == '}':
            if len(stack) > 0 and stack[-1] == 4:
                stack.pop()
            else:
                return -1
    
    if len(stack) == 0:
        return 0
    else:
        return -1

def solve():
    t = int(input())
    for i in range(0,t):
        if check() == 0:
            print("YES")
        else:
            print("NO")
solve()   