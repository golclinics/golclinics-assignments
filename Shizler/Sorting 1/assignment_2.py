# Implement a function to swap two numbers

def swap(num_1, num_2):
    print(f"Values before sawpping: num_1 = {num_1}, num_2 = {num_2}")

    num_1, num_2 = num_2, num_1

    print(f"Values after sawpping: num_1 = {num_1}, num_2 = {num_2}")


swap(2,3)