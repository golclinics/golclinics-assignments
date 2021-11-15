def reversedSentence(A):
    def reverseElements(A,start=0,stop=len(A)-1):
        while start < stop:
            A[start], A[stop] = A[stop], A[start]
            start, stop = start+1, stop-1

    # reverse whole array
    reverseElements(A)
    start = 0

    # loop through whole array reversing subsets of it(words)
    while True:
        try:
            end = A.index(' ',start,len(A))
        except:
            reverseElements(A,start,len(A)-1)
            break

        reverseElements(A, start,end-1)

        start = end + 1

    print(A)


A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reversedSentence(A)
