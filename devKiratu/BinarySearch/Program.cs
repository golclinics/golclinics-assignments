using System;

namespace BinarySearch
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var search1 = new IterativeBinarySearch();
            var nums = new int[]{1, 3, 4, 5, 10, 11, 23, 50};
            var num = 11;
            var result = search1.Exists(nums, num);
            Console.WriteLine( $"{num} exists in [{string.Join(",", nums)}]? {result}");
        }
    }
}
