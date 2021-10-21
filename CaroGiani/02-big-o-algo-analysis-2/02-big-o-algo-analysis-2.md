#Countdown
Time => f(n)=O(n)where n is the function input interger
Space => f(n) = constant

#Countdown Recursive
Time => f(n)=O(n)where n is the function input interger
Space => f(n) = constant

#Palindrome
Time => f(n)= O(n/2)  where n is len(s)
Space => f(n) = constant

#Palindrome using reversed string
Time=> f(n)= O(n)  where n is len(s)
Space => f(n) = constant

#Palindrome using recursion
Time => f(n)= O(n/2)  where n is len(s)
Space => f(n) = constant

#Concatenating arrays
Space => f(n) = O(n) where n is the sum of the size of input arrays

#Rotate an array to the left by a certain amount
Time => f(n) = O(n) where n is the sum of the lenth of A and the range of d
Space => f(n) = constant
def rotate_left(A, d):
    #deque to make it a stand queue not array
    rot_a=collections.deque(A)
    #rotate list. - for left shift + for right shit
    rot_a.rotate(-d)
    #turn back to  list from queue
    A=list(rot_a)
    return A
	
#How many times can a number be divide by 2 until we get to 1
Time => f(n) = O(log(2) n) where n is the input integer 

#Integer square root
Time => f(n) = O(n) where n is the number of values in the range 0 to x

#Integer square root bisection method
Time => f(n) = O(n/2) where n is the number of values in the range 0 to x
