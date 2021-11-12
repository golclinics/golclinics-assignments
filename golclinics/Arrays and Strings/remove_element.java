/*Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
 The relative order of the elements may be changed.

Since it is impossible to change the length of the array in some languages, you must instead have 
the result be placed in the first part of the array nums. More formally, if there are k elements 
after removing the duplicates, then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k*/


public class remove_element {
    public int removeElement(int[] nums, int val) {
       
        int actual_size=0;
        for(int i=0;i<nums.length;i++){
            if (nums[i]!=val){
                nums[actual_size]=nums[i];
                actual_size++;
            }
        }return actual_size;
        
    }
}
