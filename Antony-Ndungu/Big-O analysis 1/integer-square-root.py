#O(n) time | O(1) space
def int_sqrt(x):
    for i in range(x):
        if i * i == x:
            return i
    
    return -1
