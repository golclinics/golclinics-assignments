def minSwaps(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}
     
    # Initialize result
    # number of swaps = number of nodes - 1
    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i
         
        while not vis[j]: 
            # node is now visited
            vis[j] = True 
            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
             
        # update answer by adding
        # current cycle
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans
     
arr = [1, 5, 4, 3, 2]
print(minSwaps(arr))