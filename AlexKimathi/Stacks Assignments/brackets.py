def isBalanced(S):
    stack = []
    pairs = {"{": "}", "[": "]", "(" : ")"}
    for i in S:
        if not stack:
            stack.append(i)
        elif i == pairs.get(stack[-1]):
            stack.pop()
        else:
            stack.append(i)
    return "YES" if not stack else "NO"

for i in range(int(input())):
    S = input()
    print(isBalanced(S))
    