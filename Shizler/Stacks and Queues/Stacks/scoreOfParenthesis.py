# Given a balanced parentheses string s, return the score of the string.
# 	The score of a balanced parentheses string is based on the following rule:
# 	"()" has score 1.
# 	AB has score A + B, where A and B are balanced parentheses strings.
# 	(A) has score 2 * A, where A is a balanced parentheses string.
# 	Examples:
# 	Input: s = "()"
# 	Output: 1
# 	Input: s = "(())"
# 	Output: 2
# 	Input: s = "()()"
# 	Output: 2
# 	Input: s = "(()(()))"
# 	Output: 6
def scoreOfParenthesis(s):
    stack = []
    count=0
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        if bracket == ')':
            stack.pop()
            count+=1
    return count
if __name__ == '__main__':
    ss = ["()","(())","()()","(()(()))"]
    for s in ss:
        print(scoreOfParenthesis(s))