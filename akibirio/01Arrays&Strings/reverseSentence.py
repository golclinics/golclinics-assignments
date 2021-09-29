# function to reverse an array

def reversesentence(arra):
    space = ' '
    order_at = arra.index(space)
    ordered_list = arra[order_at:] + arra[:order_at]
    for word in ordered_list:
        word = ordered_list[order_at:] + ordered_list[:order_at]
    return word


if __name__ == '__main__':
    array = ['I', ' ', 'l','i','k','e', ' ', 'c','o','d','e']
    print(array)
    #reversesentence(array)
    print()
    print("Reversing String now ... ")
    print(reversesentence(array))

