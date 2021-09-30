#include <stdio.h>

void print(char *A, size_t length, char *description);
void swap(char *a, char *b);
void reverseArray(char *A, size_t startIndex, size_t endIndex);
void reverseSentence(char *A, size_t length);

int main(void){
    char A[] ={'t','h','i','s',' ','i','s',' ','g','o','o','d'};
    size_t length = sizeof(A)/sizeof(char);
    print(A, length, "Before");
    reverseSentence(A,length);
    print(A, length, "After");
}

void print(char *A, size_t length, char *description){
    printf("%s: [", description);
    for(size_t i = 0; i < length; i++){
        printf("'%c'", A[i]);
        if(i == length - 1)
            continue;
        printf(", ");
    }
    printf("]\n");
}

void swap(char *a, char *b){
    char temp = *a;
    *a = *b;
    *b = temp;
}

void reverseArray(char *A, size_t startIndex, size_t endIndex){
    for(size_t i = startIndex, j = endIndex; i < j; i++, j--)
        swap(A+i, A+j);
}

void reverseSentence(char *A, size_t length){
    //Reverse sentence
    reverseArray(A, 0, length -1);
    size_t startOfWord = 0, endOfWord = 0;
    // Traverse the sentence, reversing each word
    for(size_t i = 0; i < length; i++){
        if(A[i] == ' '){
            endOfWord = i - 1;
            reverseArray(A, startOfWord, endOfWord);
            startOfWord = i + 1;
            continue;
        }
        if(i == length - 1){
            reverseArray(A, startOfWord, length-1);
        }
    }
}