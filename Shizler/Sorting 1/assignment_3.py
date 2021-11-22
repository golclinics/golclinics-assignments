# time complexity - O(n^2) - worst case is having the least number at end of array, meaning iterating the whole length of array twice
# space complexity - O(1) - no auxiliary  space

def insertion_sort(arrayN):
    for i in range(1,len(arrayN)):
        key = arrayN[i]

        j = i - 1

        while j>=0 and key < arrayN[j]:
            arrayN[j+1] = arrayN[j]
            j-=1
        
        arrayN[j+1] = key
    return arrayN


print(insertion_sort([5,8,2,6,74,1,5,8, 82]))