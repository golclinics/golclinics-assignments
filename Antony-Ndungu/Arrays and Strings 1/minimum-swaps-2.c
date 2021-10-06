#include <stdio.h>

int minimumSwaps(int *arr, size_t arrSize);

int main(void){
    int nums[] = {2, 3, 4, 1, 5};
    size_t numsSize = sizeof(nums) / sizeof(int);
    printf("%d\n", minimumSwaps(nums, numsSize));
    return 0;
}

int minimumSwaps(int *arr, size_t arrSize){
    int numSwaps = 0, index = 0, swapIndex, temp;
    while(index < arrSize){
        if(index + 1 != arr[index]){
            swapIndex = arr[index] - 1;
            temp = arr[swapIndex];
            arr[swapIndex] = arr[index];
            arr[index] = temp;
            numSwaps++;
        }else{
            index++;
        }
    }
    return numSwaps;
}