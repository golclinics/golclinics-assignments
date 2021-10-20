def removeElement(inputNum, val):
    if ( not inputNum ) or ( inputNum == 0 ):
        exit("The array list can not be empty")

    if ( not val ) or ( str(val).isdigit() == False ):
        exit("val cannot be empty or must be a digit")

    counter = 0
    for num in inputNum:
        if (str(num).isdigit() == False):
            exit("The array can only be number") 
        if num < 0:
            exit("The array list can not be less than 0")
        #Check if value exist in the list
        if (num != val):
            counter += 1
    return counter

inputNum = [0,1,2,2,3,0,4,2]
val = 2

print(removeElement(inputNum, val))