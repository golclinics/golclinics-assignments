#include <stdio.h>

int removeElement(int* nums, int numsSize, int val);

int main(void){
    int nums[] = {3,2,2,3};
    int numsSize = (int) sizeof(nums)/sizeof(int); 
    numsSize =  removeElement(nums, numsSize, 3);
    printf("size of nums: %d\n",numsSize);
    printf("elements in nums: ");
    for(size_t i = 0; i < numsSize; i++)
        printf("%d ", nums[i]);
    printf("\n");
    return 0;
}

int removeElement(int* nums, int numsSize, int val){
    size_t i = 0;
    while(i<numsSize){
        if(val == nums[i]){
            nums[i] = nums[numsSize - 1];
            numsSize--;
            continue;
        }
        i++;
    }
}