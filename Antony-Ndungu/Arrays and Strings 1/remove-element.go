package main

import "fmt"

func main() {
	nums := []int{3, 2, 2, 3}
	nums = nums[0:removeElement(nums, 3)]
	fmt.Println(nums)
}

func removeElement(nums []int, val int) int {
	var i int
	k := len(nums)
	for i < k {
		if val == nums[i] {
			nums[i] = nums[k-1]
			k--
			continue
		}
		i++
	}
	return k
}
