# Write a function reverseArray(A) that takes in an array A and reverses it, 
# without using another array or collection data structure i.e. in-place.

def reverseArray(arr):
    n = len(arr)
    
    for i in range(n//2):
      arr[i], arr[n-1-i] = arr[n-1-i], arr[i]


# Test function
if __name__ == "__main__":
  myArray = [10, 5, 7, 6, 9]
  reverseArray(myArray)
  print(myArray)