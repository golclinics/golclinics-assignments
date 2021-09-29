# function to reverse an array

def reverse(arra):
    size = len(arra)
    right = size - 1
    iterations = size//2

    if len(arra) == 0:
        return

    for i in range(0, iterations):
        temp = arra[right]
        arra[right] = arra[i]
        arra[i] = temp
        right -= 1


if __name__ == '__main__':
    array = [6, 5, 8, 3]
    print(array)
    reverse(array)
    print()
    print("Reversing Array now ... ")
    print(array)

