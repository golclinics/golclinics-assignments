using System;
using System.Collections.Generic;

namespace _2Nums
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nums = {2,7,11,15};
            int[] nums2 ={3,2,4};
            int[] nums3 = {3,3};
            Console.WriteLine(getIndex(nums,9));
            Console.WriteLine(getIndex(nums2,6));
            Console.WriteLine(getIndex(nums3,6));
        }
        public static string getIndex(int[] nums, int target){
            var hs = new HashSet<int>();
            string result = "";
            int n = nums.Length;

            for(int i=0;i<n;i++){
                int diff = target - nums[i];
                if(hs.Contains(diff)){
                    result +=  Array.IndexOf(nums,diff) +","+ i; 
                }else{
                    hs.Add(nums[i]);
                }
            }

            return result;
        }
    }
}
