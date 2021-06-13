import timeit

n = 10
def countdown(n):
  while n> 0:
    print(n)
    n -= 1
  print("Blast Off!")

countdown(n)
testcode = ''' 
n = 10
def countdown(n):
  while n> 0:
    print(n)
    n -= 1
  print("Blast Off!")
'''
print(timeit.timeit(stmt=testcode))
#This algorithm has a linear time complexity[0(n)]. Run time increases linearly with the size of the input data. 
# The algorithm's space complexity is constant 0(1) as number of iterations is a constant regardless of how large the array is.

def countdown_recursive(n):
    if n == 0:
        print("Blast Off!")
    else:
        print(n)
        countdown_recursive(n-1)

countdown_recursive(n)

#This algorithm has a linear time complexity[0(n)]. Run time increases linearly with the size of the input data. 
# The algorithm has a linear space complexity.

"""The space complexities of the two algorithms are different because 
If you use a recursive approach, 
then at each stage, you have to make a recursive call. That means
 leaving the current invocation on the stack,
 and calling a new one. When you're k levels deep, you've got k lots of stack frame, 
 so the space complexity ends up being proportional to the depth you have to search.

With your iterative code, you're allocating one variable (O(1) space)
 plus a single stack frame for the call (O(1) space).
  Your while loop doesn't ever allocate anything extra, 
  either by creating new variables or object instances, 
  or by making more recursive calls. So the only space you need, 
  for your whole call, is the O(1) space taken up by the variable
   you create and the rest of the stack frame"""

s = 'madam'
def is_palindrome(s):
    if len(s) == 0:
        return True   # an empty string is a palindrome

    size = len(s)
    midpoint = size // 2
    
    for i in range(midpoint + 1):
        if s[i] != s[size - i - 1]:
            return False
    return True
print(is_palindrome(s))

#The space required will also depend on the size and content of the input.  Therefore, the algorithm requires O(n) space.
# The algorithm is linear hence the time complexity evn in worst case scenario is 0(n)


def is_palindrome_rev(s):
    reversed_s = s[::-1] 
    return s == reversed_s
print(is_palindrome_rev(s))
def is_palindrome_rev2(s):
    reversed_seq = reversed(s) 
    reversed_s = ''.join(reversed_seq) 
    return s == reversed_s
print(is_palindrome_rev2(s))

# Time complexity - There are a total of N/2 swap calls required for a list reversal, where N is the total number of items in the list. Since swap is a constant time operation, the overall time complexity is O(N/2), which is same as O(N).
# Space complexity - is also 0(n)


def is_palindrome_recur(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return True
    return s[0] == s[-1] and is_palindrome_recur(s[1:-1])
print(is_palindrome_recur(s))

#Time complexity is 0(n)
#Space complexity is 0(n)

import timeit

s = "m" * 500 + "u" + "m" * 500 # this creates a string with 1001 characters, 500 'm' followed by a 'u' followed by 500 'm'.

# This will execute is_palindrome(s) 1000 times and return the average execution time in seconds
result = timeit.timeit(lambda: is_palindrome(s), number=1000) 
print("is_palindrome time:", result)
result = timeit.timeit(lambda: is_palindrome_rev(s), number=1000) 
print("is_palindrome_rev time:", result)
result = timeit.timeit(lambda: is_palindrome_rev2(s), number=1000) 
print("is_palindrome_rev2 time:", result)
result = timeit.timeit(lambda: is_palindrome_recur(s), number=1000) 
print("is_palindrome_recur time:", result)

# I would prefer is_palindrome_rev as The built-in C function is much faster than the pure python loop as shown by the analysis.
# The results matched my expectations.

A = [1, 2, 3, 4, 5]
B = [6, 7, 8, 9, 10]

def concatenate_arrays(A, B):
    result = []
    for x in A:
        result.append(x)
    for y in B:
        result.append(y)
    return result
print(concatenate_arrays(A, B))

#Time and space complexities are 0(n)

A = [3, 2, 1, 10, 15, 3] 
d = 3
def rotate_left(A, d):
    for _ in range(d):
        first_item = A[0]
        for i in range(len(A)):
            A[i] = A[i + 1]
        A[-1] = first_item

# Nested for loop has a quadratic time complexity, that is, 0(n**2)
# Algorithm uses constant, or O(1), auxilliary space hence its a constant space complexity.


# Better way?????
n= 4
def count_div_2(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
print(count_div_2(n))

#Time complexity - 0(n)
#Space Complexity - Due to creating variables, and updating the values of variables inside of an iteration it is 0(n)


x = 45
def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1

print(int_sqrt(x))

#This algorithm has a linear time complexity[0(n)]. Run time increases linearly with the size of the input data. 
# The algorithm's space complexity is constant 0(1) as number of iterations is a constant regardless of how large the array is.
def int_sqrt_bisect(x):
    low = 0
    high = x
    guess = x // 2
    while True:
        diff = guess * guess - x
        if diff == 0:
            return guess
        if diff < 0: 
            low = guess 
        else: 
            high = guess 
        
        if high - low <= 1:
            break

        guess = (low + high) // 2 
    return -1

#This algorithm has a linear time complexity[0(n)]. Run time increases linearly with the size of the input data. 
# The algorithm's space complexity is constant 0(n) too.