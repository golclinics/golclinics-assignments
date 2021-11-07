import java.util.HashMap;


public class AddsToTarget {

    public int[] indexOfNumbersThatAddToTarget(int[] nums, int target){
        HashMap<Integer, Integer> indices = new HashMap<>();

        int n = nums.length - 1;
        for(int i = 0; i <= n; i++){
            int compliment = target - nums[i];

            if(indices.containsKey(compliment)){
                System.out.println("["+indices.get(compliment) + " , " + i+"]");
                return new int[] {indices.get(compliment), i};
            }

            indices.put(nums[i], i);


        }

        throw new IllegalArgumentException("There are no numbers that add up to target");

    }
    public static void main(String[] args) {
        AddsToTarget addsToTarget= new AddsToTarget();
        int[] nums = {3,2,4};
        int[]  nums2 = {3,3};
        int[] nums3 = {2,7,11,15};
        addsToTarget.indexOfNumbersThatAddToTarget(nums3, 9);
    }
}
