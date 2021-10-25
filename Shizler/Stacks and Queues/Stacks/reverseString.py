def reverseString(s):
    stack = [] #create new stack
    new_s = ''
    # add all chars to stack
    for i in s:
        stack.append(i)

    # remove chars from stack and add them to string
    for i in s:
        popped = stack.pop()
        new_s = new_s + popped

    print(new_s)

s = 'qwerty'
reverseString(s)