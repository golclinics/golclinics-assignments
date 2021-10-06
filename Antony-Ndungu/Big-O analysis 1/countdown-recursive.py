# O(n) time | O(n) space because each recursive call results in a new stack/function frame on the call stack with its own value of n.
# by the time the function is at it's base case the memory space utilised at that point is directly proportional to the size of n.
def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)
