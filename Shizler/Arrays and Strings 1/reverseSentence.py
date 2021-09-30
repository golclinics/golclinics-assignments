def reversedSentence(A):
    matrix_arr = []
    tempArr = []
    # separate the words with a 2d array
    for i in range(len(A)):
        if (A[i] == ' ') and len(tempArr) != 0:
            matrix_arr.append(tempArr)
            tempArr = []
        else: 
            tempArr.append(A[i])
    
    if len(tempArr) != 0:
        matrix_arr.append(tempArr)

    # reverse the words
    matrix_arr.reverse()

    # revert the array back to 1d array
    finalArr = []
    for i in range(len(matrix_arr)):
        for j in range(len(matrix_arr[i])):
            finalArr.append(matrix_arr[i][j])
            if j == (len(matrix_arr[i])-1):
                finalArr.append(' ')

    print(finalArr)


A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
reversedSentence(A)
