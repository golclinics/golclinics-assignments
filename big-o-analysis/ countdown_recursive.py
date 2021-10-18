def countdown_recursive(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        countdown_recursive(n - 1)


# **************  TIME COMPLEXITY  **************
# The time complexity is O(n)


# **************  SPACE COMPLEXITY  **************
# The space complexity is O(n)