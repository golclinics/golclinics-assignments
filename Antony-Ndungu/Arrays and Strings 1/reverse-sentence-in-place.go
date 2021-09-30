package main

import (
	"fmt"
)

func main() {
	A := []byte{'t', 'h', 'i', 's', ' ', 'i', 's', ' ', 'g', 'o', 'o', 'd'}
	print(A, "Before")
	reverseSentence(A)
	print(A, "After")
}

func print(A []byte, description string) {
	fmt.Printf("%s: [", description)
	for i, c := range A {
		fmt.Printf("'%c'", c)
		if i == len(A)-1 {
			continue
		}
		fmt.Printf(",")
	}
	fmt.Printf("]\n")
}

func reverseArray(A []byte, startIndex int, endIndex int) {
	for i, j := startIndex, endIndex; i < j; i, j = i+1, j-1 {
		A[i], A[j] = A[j], A[i]
	}
}

func reverseSentence(A []byte) {
	// Reverse the characters in the sentence
	reverseArray(A, 0, len(A)-1)
	//Traverse the sentence, reversing each word in the sentence
	var startOfWord, endOfWord int
	for i := 0; i < len(A); i++ {
		if A[i] == ' ' {
			endOfWord = i - 1
			reverseArray(A, startOfWord, endOfWord)
			startOfWord = i + 1
			continue
		}
		if i == len(A)-1 {
			reverseArray(A, startOfWord, len(A)-1)
		}
	}
}
