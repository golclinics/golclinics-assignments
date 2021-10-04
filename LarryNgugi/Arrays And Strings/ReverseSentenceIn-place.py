# Function to reverse each word in the string

def reverse_word(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start = start + 1
        end -= 1
 
 
A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
 
# Convert string to list to use it as a char array

A = list(A)
start = 0
while True:
     
   
    try:
        end = A.index(' ', start)

        reverse_word(A, start, end - 1)
 
        start = end + 1
 
    except ValueError:
 
        reverse_word(A, start, len(A) - 1)
        break
 
A.reverse()
 
def Convert(string):
    A=[]
    A[:0]=string
    return A

A = "".join(A)
 
print("The Reversed sentence is : ",Convert(A))
 

