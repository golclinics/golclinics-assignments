package main

import "fmt"

func main() {
	nums := []int{2, 3, 4, 1, 5}
	fmt.Println(minimumSwaps(nums))
}

func minimumSwaps(nums []int) int {
	var numSwaps, index int
	for index < len(nums) {
		if (index + 1) != nums[index] {
			nums[index], nums[nums[index]-1] = nums[nums[index]-1], nums[index]
			numSwaps++
		} else {
			index++
		}
	}
	return numSwaps
}
