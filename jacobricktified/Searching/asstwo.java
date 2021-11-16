class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] ans = new int [2];
		Map<Integer,Integer> complimentmap = new HashMap<>();
		for(int i=0;i<nums.length;i++) {
			int compliment  = target-nums[i];
			if(complimentmap.containsKey(compliment)) {
				ans = new int [] {complimentmap.get(compliment),i};
				break;
			}
			complimentmap.put(nums[i],i);
		}
		return ans;
    }
}