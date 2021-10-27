def twoNum(arr, target):
    numToIndex = map(lambda x: x, arr)

    n = len(arr)
    newArr = []

    for i in range(n):
        complement = target - arr[i]
        if complement in numToIndex:
            newArr.append(complement)
    return newArr

print(twoNum([8, 1, 2, 7, 11, 15, 22, 5, 4, ], 9))