using System;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            // var search1 = new IterativeBinarySearch();
            var searchRecursive = new RecursiveBinarySearch();
            var nums = new int[]{1, 3, 4, 5, 10, 11, 23, 50};
            var num = 10;
            var firstIndex = 0;
            var lastIndex = nums.Length-1;
            var result = searchRecursive.Exists(nums, num, firstIndex, lastIndex);
            Console.WriteLine( $"{num} exists in [{string.Join(",", nums)}]? {result}");
        }
    }
}
