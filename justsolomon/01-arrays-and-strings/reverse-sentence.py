def reverseSentence(A):
	def reverseWord(start, end):
		if start > end:
			return
	
		while start < end:
			A[start], A[end] = A[end], A[start]
			
			start += 1
			end -= 1
	
	
	currentStart = 0
	length = len(A)
	
	reverseWord(0, length - 1)
	
	for i in range(length):
		if A[i] == " ":
			reverseWord(currentStart, i - 1)
			currentStart = i + 1
		elif i == length - 1:
			reverseWord(currentStart, i)
	
	return A