using System;

namespace BinarySearch
{
    public class IterativeBinarySearch
    {
    //nums -> [1, 3, 4, 5, 10, 11, 23, 50]
    //search if an element exists in the sorted collection using an iterative Binary search
    public bool Exists(int[] nums, int num)
    {
      var startIndex = 0;
      var lastIndex = nums.Length - 1;
      while(startIndex <= lastIndex)
      {
        var midpoint = GetMidIndex(startIndex, lastIndex);
        if (nums[midpoint] == num)
        {
          return true;
        }
        else if(num < nums[midpoint])
        {
          lastIndex = midpoint-1;
        }
        else 
        {
          startIndex = midpoint+1;
        }

      }
      
      return false;
    }

    private int GetMidIndex(int firstIndex, int lastIndex)
    {
      var index = (int)Math.Truncate((double)(lastIndex - firstIndex) / 2);
      return index + firstIndex;
    }
  }
}
