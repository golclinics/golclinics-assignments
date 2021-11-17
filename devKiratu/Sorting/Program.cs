using System;

namespace Sorting
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var sorting = new SortingAssignments();
            var arr1 = new int[]{3,5,2,1,4};
            var arr2 = new int[]{1,1,2,3,4,5};

            Console.WriteLine($"Is [{string.Join(",",arr1)}]? {sorting.IsSorted(arr1)}");
            Console.WriteLine($"Is [{string.Join(",",arr2)}]? {sorting.IsSorted(arr2)}");
        }
    }
}
