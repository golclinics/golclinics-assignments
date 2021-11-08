namespace Searching
{
    public class TwoIndices
    {
      //Input: nums = [2,7,11,15], target = 9 Output: [0,1].
      //Input: nums = [3,2,4], target = 6 Output: [1,2]
      //Input: nums = [3,3], target = 6 Output: [0,1]
        private int a,b = 0;
        public int[] AddUpToTarget(int[] array, int target)
        {
          for(var i = 0; i < array.Length; i++)
          {
            for(var j = i+1; j < array.Length; j++)
            {
              if(array[i] + array[j] == target)
              {
                a = i;
                b = j;
                i = array.Length;
                break;
              }
            }
          }

          return new int[]{a,b};
        }
    }
}
