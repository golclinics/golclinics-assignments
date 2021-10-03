
const removeElement = (nums, val) => {
    let n = nums.length
    let i = 0;
    for(i; i < n; i++){
        if(nums[i] == val){
            nums[i] = null
        }
    }
   
    for(let j = 0; j < n; j++){
        let temp = nums[n - 1];
        if(nums[j] == null && nums[n-1] != null){
            nums[j] = temp;
            nums[n-1] = null
            n--
        }else if(nums[j] == null && nums[n-1] == null){
          n--
        }
    }
    console.log(nums)
}

removeElement([3,2,2,3, 3], 2);


