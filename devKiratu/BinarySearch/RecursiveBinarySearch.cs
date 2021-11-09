using System;

namespace BinarySearch
{
    public class RecursiveBinarySearch
    {
      //nums -> [1, 3, 4, 5, 10, 11, 23, 50]  
      //search if an element exists in the sorted collection using using a recursive Binary search
        public bool Exists(int[] nums, int num, int startIndex, int lastIndex)
        {
          if (startIndex > lastIndex)
          {
            return false;
          } 

          var midpoint = GetMidIndex(startIndex, lastIndex);
          if (nums[midpoint] == num)
          {
            return true;
          }
          else if(num < nums[midpoint])
          {
            lastIndex = midpoint-1;
            return Exists(nums, num, startIndex, lastIndex);
          }
          else 
          {
            startIndex = midpoint+1;
            return Exists(nums, num, startIndex, lastIndex);
          }
        }

        private int GetMidIndex(int firstIndex, int lastIndex)
        {
          var index = (int)Math.Truncate((double)(lastIndex - firstIndex) / 2);
          return index + firstIndex;
        }
    }
}
