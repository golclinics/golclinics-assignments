#Main Approach
#Reversing the array by using the swapping method, swap the value of the first index with that of the last index and vice versa -we use a while loop bc we don't know the range of the array
def reverse_array(A):
  start_index = 0
  final_index = len(A) -1 #following the principle that an arrays are zero based therefore -1
  while start_index < final_index:
    A[start_index], A[final_index] = A[final_index],A[start_index]
    start_index += 1
    final_index = final_index - 1
  return A
print(reverse_array([1,2,3,4])) 




#The following methods are different solution approaches after the first main approach
#reversing using the reversed built in method in python
def reverse_array(A):
  revers = reversed(A) #returns an iterator object therefore use list to make a list out of the object
  return list(revers)
print(reverse_array([1,2,3,4]))

#reversing using the reverse built in method
def reverse_array(A):
  A.reverse()
  return A
  
print(reverse_array([1,2,3,4])) 

#reversing using the slicing method
def reverse_array(A):
  return A[::-1]
print(reverse_array([1,2,3,4]))
 

#reversing by insertion - the element is therefore always added at the 0th position hence reversed
def reverse_array(A):
  temp =[]
  for i in A:
    temp.insert(0,i)
  return temp  
print(reverse_array([1,2,3,4]))    

