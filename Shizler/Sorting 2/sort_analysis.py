# Compute the time and space complexity of the 3 sort algorithms implemented today.

class NumSort:
  
  def __init__(self,arr):
      self.arr = arr
      self.resArray = []

  # Insertion sort
  # time complexity - O(n^2) 
  # space complexity - O(1) - no extra  space
  def insertion_sort(self):
    for i in range(1, len(self.arr)):
        keyValue = self.arr[i]

        j = i - 1

        while j >= 0 and keyValue < self.arr[j]:
            self.arr[j + 1] = self.arr[j]
            j -= 1
        
        self.arr[j + 1 ] = keyValue
    return self.arr

  # bubble sort
  # time complexity - O(n^2) 
  # space complexity - O(1) - no extra  space
  def bubble_sort(self):
    for i in range(len(self.arr)):
        for j in range(i+1, len(self.arr)):
            if self.arr[i] > self.arr[j]:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
    return self.arr

  # selection sort
  # time complexity - O(n^2) 
  # space complexity - O(1) - no extra  space
  def selection_sort(self):
    while len(self.arr):
        minValue = min(self.arr)
        self.resArray.append(minValue)
        self.arr.remove(minValue)

    return self.resArray

num_sort = NumSort([5,8,2,6,74,1,5,8,82])

print(num_sort.insertion_sort())
print(num_sort.bubble_sort())
print(num_sort.selection_sort())
