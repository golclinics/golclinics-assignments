using System.Collections.Generic;
namespace Sorting
{
    public class SortingAssignments
    { /*
        Assignment one: How do you check if a collection sorted 
        (Implement a function to check a collection is sorted)
        [3,5,2,1,4]
        [1,2,3,4,5]
      */
        public bool IsSorted(int[] array)
        {
            var results = new List<bool>();
            for(var i = 1; i < array.Length; i++)
            {
                if (array[i] >= array[i-1])
                {
                    results.Add(true);
                }
            }
            return results.Count == array.Length-1;
        }
    }
}
