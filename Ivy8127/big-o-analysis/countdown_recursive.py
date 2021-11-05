""" def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1) """

Time complexity => O(n) 
Space complexity => O(n) bc at each recursive call, we are adding it to a call stack memory till the base case is reached