def reverseArray(A):
	start = 0
	end = len(A) - 1
	
	while start < end:
		A[start], A[end] = A[end], A[start]
		
		start += 1
		end -= 1
	
	return A
