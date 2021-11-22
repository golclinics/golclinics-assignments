# time complexity - O(nlogn) 
# space complexity - O(1) - no extra  space
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)// 2

        l = arr[:mid]
        r = arr[mid:]

        merge_sort(l)
        merge_sort(r)

        i = j = k = 0

        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k+=1
        
        while i < len(l):
            arr[k] = l[i]
            i+=1
            k+=1
        while j < len(r):
            arr[k] = r[j]
            j+=1
            k+=1
    return arr
arr = [9,7,3,6,2]

print(merge_sort(arr))
        
