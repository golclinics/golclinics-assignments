# Assignments

	Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
	
	Implement the MinStack class:
	
	MinStack() initializes the stack object.
	void push(int val) pushes the element val onto the stack.
	void pop() removes the element on the top of the stack.
	int top() gets the top element of the stack.
	int getMin() retrieves the minimum element in the stack.
	 
	Example:
	
	Input
	["MinStack","push","push","push","getMin","pop","top","getMin"]
	[[],[-2],[0],[-3],[],[],[],[]]
	
	Output
	[null,null,null,null,-3,null,0,-2]                                                                                                                                                                          
	Given a balanced parentheses string s, return the score of the string.
	
	The score of a balanced parentheses string is based on the following rule:
	
	"()" has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.
	 
	Examples:
	
	Input: s = "()"
	Output: 1
	
	Input: s = "(())"
	Output: 2
	 
	Input: s = "()()"
	Output: 2