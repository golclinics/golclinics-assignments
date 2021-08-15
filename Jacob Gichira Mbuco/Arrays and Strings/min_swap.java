/* You are given an unordered array consisting of consecutive integers 
 [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any
 two elements. Find the minimum number of swaps required to sort the array 
 in ascending order.

Example


Perform the following steps:

i   arr                         swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]
It took  swaps to sort the array */
static int minimumSwaps(int[] arr) {
    int len = arr.length;
    int count = 0;
    for (int i=0;i<len;i++){
        int numlookingfor = i+1;
        if(arr[i]!= numlookingfor){
            for(int j=i+1;j<len;j++){
                if(arr[j]==numlookingfor){
                    int temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}