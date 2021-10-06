package main

import "fmt"

func main() {
	A := []int{10, 5, 6, 9}
	fmt.Println("Before:", A)
	reverseArray(A)
	fmt.Println("After:", A)
}

func reverseArray(A []int) {
	for i, j := 0, len(A)-1; i < len(A)/2; i, j = i+1, j-1 {
		A[i], A[j] = A[j], A[i]
	}
}
