#include <stdio.h>

void print(int *array, size_t size);
void swap(int *x, int *y);
void reverseArray(int *array, size_t size);

int main(void){
    int A[] = {10, 5, 6, 9};
    size_t lengthOfA = sizeof(A) / sizeof(int);
    printf("Before: ");
    print(A, lengthOfA);

    reverseArray(A, lengthOfA);
    printf("After: ");
    print(A, lengthOfA);
    return 0;
}

void print(int *array, size_t size){
    printf("[");
    for(size_t i = 0; i < size; i++){
        printf("%d", array[i]);
        if(i == size-1)
            continue;
        printf(", ");
    }
    printf("]\n");
}

void swap(int *x, int *y){
    int temp = *x;
    *x = *y;
    *y = temp;
}

void reverseArray(int *array, size_t size){
    for(size_t i = 0, j = size - 1; i < size/2; i++, j--){
        swap(array+i, array+j);
    }
}