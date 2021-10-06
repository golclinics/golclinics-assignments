package main

import "fmt"

func main() {
	nums := []int{3, 2, 2, 3}
	nums = nums[0:removeElement(nums, 3)]
	fmt.Println(nums)
}

func removeElement(nums []int, val int) int {
	var i int
	for i < len(nums) {
		if val == nums[i] {
			nums[i] = nums[len(nums)-1]
			nums = nums[:len(nums)-1]
			continue
		}
		i++
	}
	return len(nums)
}
