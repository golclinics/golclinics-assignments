#Write a function reverseArray(A) that takes in an array A and reverses it, 
# without using another array or collection data structure; in-place.
#A = [10, 5, 6, 9]
#reverseArray(A)
#import numpy as np
def reverseArray(A):
    l = len(A)
    i = 0
    while i<l:
        A[i],A[l-1]=A[l-1],A[i]
        i+=1
        l-=1
    print(A)


A=[10,5,6,9]
reverseArray(A)
