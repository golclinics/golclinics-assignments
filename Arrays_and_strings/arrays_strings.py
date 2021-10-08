##Array

"""Write a function reverseArray(A) that takes in an array A and reverses it, 
without using another array or collection data structure; in-place"""

A = [1, 4, 5, 6, 5]

print(A[::-1])
#print(A.reverse) -  which one is right.

def reverse_array(A):
    start_index = 0
    end_index = len(A) - 1
    
    while end_index > start_index:
        A[start_index], A[end_index] = A[end_index], A[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

if __name__ == '__main__':
    A = [10, 6, 9, 7]
    reverse_array(A)
    print(A)


"""Write a function reverseSentence(A) that takes in an array of characters
, A, and reverses the the "words" (not individual characters).

Example:

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A) A // ['g','o','o','d',' ','i','s',' ','t','h','i','s']
"""
D = ['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd']


def reverseSentence(D):
    a = ''.join(D).split()
    b = a[::-1]
    c = ' '.join(b)
    return list(c)


print(reverseSentence(D))


def  reverseSentence(A):
	

	#join the indiviatual words eg good 
	#there are spaces after every indivitual words
	#join the words in the event a space is encountered 
	#use the isspace method --returns true if there is a whitespace 

	#convert the list to a string 
	for i in range(len(A)):
		if A[i].isspace()==False:
			#join the characters with no space
			A=''.join(A)
		elif A[i].isspace()==True:
			#replace the spaces with a comma 
			A=A.replace(' ',',')

	A=list(A.split(','))
	#print(A)
	#print(len(A))
	#use the split function to create a new array of words 
	
	length=len(A)//2
	rev=-1
	reverseLength=-(length)#make it anegative value
	for i in range(length):
		if i!=0:
			rev=rev-1# to move from the last to the first as you swap
		A[i],A[rev]=A[rev],A[i]

		if rev==reverseLength:
			break
			#termonate the loop since swapping operation is over
	print(A)		#GET THE REVESED ARRAY 

	#make the list of words to a list of characters 
	A=''.join(A)
	A=list(A)
	print(A)

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reverseSentence(A)


#hackerrank - algorithm called bubble sort.
#What does in space mean?
"""
You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates.
You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in
ascending order.
Example
Perform the following steps:
i   arr [7, 1, 3, 2, 4, 5, 6] swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array.
"""
def minimumSwaps(arr):
    swaps = 0
    tmp = {}

    for i, val in enumerate(arr):
        tmp[val] = i

    for i in range(len(arr)):
        # because they are consecutives, I can see if the number is where it belongs
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t

            # Switch also the tmp array, no need to change i+1 as it's already good now
            tmp[t] = tmp[i+1]

    return swaps

print(minimumSwaps([7, 1, 3, 2, 4, 5, 6]))

##leetcode - remove element
"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have
the result be placed in the first part of the array nums. More formally, if there are k elements 
after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array 
in-place with O(1) extra memory.
"""
#Time Complexity - Since there is a single scan of the array, the time complexity will be O(n).

#Space Complexity -We are not using any data structure for internal computations, hence the space complexity will be O(1).

from typing import List


class RemoveElement:
    @staticmethod
    def removeElement(nums: List[int], val: int) -> int:
        # Counter for keeping track of elements other than val
        count = 0
        # Loop through all the elements of the array
        for i in range(len(nums)):
            if nums[i] != val:
                # If the element is not val
                nums[count] = nums[i]
                count += 1
        return count


if __name__ == '__main__':
    r = RemoveElement()
    print(r.removeElement([2, 3, 3, 2], 3))
    print(r.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))


def removeElement(self, nums, val):
    length = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[length] = nums[i]
            length += 1

    return length

print(r.removeElement([2, 3, 3, 2], 3))
print(r.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))
