def reverseA(arr):

  arr_len = len(arr) - 1
  
  for i in range(len(arr)//2):
        temp = arr[i]
        arr[i] = arr[arr_len - i]
        arr[arr_len - i] = temp

  return arr

print(reverseA([9,4,6,4,3,4,10,8,9,5,67]))
