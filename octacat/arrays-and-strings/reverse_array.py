#Write a function reverseArray(A) that takes in an array A and reverses it, 
#without using another array or collection data structure; in-place.

def reverseArray(A):
    if len(A) == 0:
        print("A can not be empty")
        return

    #Begining of the index
    start_index = 0

    #End of the index - 1 
    end_index = len(A) - 1

    #Swamp elements
    while end_index > start_index:
        A[start_index], A[end_index] = A[end_index], A[start_index]
        start_index += 1
        end_index -= 1
    return(A) 
        

A = [10, 5, 6, 9, 10, 3, 1, 8]
print("The original list")
print(A)
print("")
print("The reverse list")
print(reverseArray(A))