def min_swap(l):
    if ( not l ) or ( l == 0 ):
        exit("The array list can not be empty")

    sorted_list = l.copy()
    sorted_list.sort()

    h = {}
    for i, v in enumerate(sorted_list):
        h[v] = i

    minimum_swap = 0
    for pos, v in enumerate(l):
        while True:
            v = l[pos]
            final_pos = h[v]
            if pos == final_pos:
                break
            else:
                l[pos],l[final_pos] = l[final_pos], l[pos]
                minimum_swap += 1 
    return(minimum_swap)

print(min_swap([1,2,8,9,5,3]))