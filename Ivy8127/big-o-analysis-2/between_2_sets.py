def getTotalX(a, b):
    # Write your code here
    maxA = max(a)
    minB = min(b)
    count = 0
    for i in range(maxA, minB+1):
        if all([i%j==0 for j in a]):
            if all([j%i==0 for j in b]):
                count += 1
    return count