# Time Complexity
# The time complexity is linear
# The number of operation increases proportionaly with increase in the value of input
# The trend would be linear


# Example
# number > 10
# The number of operations are 10 loops
def countDown(n):
    while n > 0:
        print(n)         # O(1)
        n -=1            # O(1)
    print("Blast off")

countDown(5)

# Time Complexity => O(N) + 2 O(1)
# we are interested with the worst case scenario

# Time complexity is therefore O(N) where n is the number passed to the
# function.
