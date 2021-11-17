using System;

namespace Sorting
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            //Assignment One
            var sorting = new SortingAssignments();
            var arr1 = new int[]{3,5,2,1,4};
            var arr2 = new int[]{1,1,2,3,4,5};

            Console.WriteLine($"Is [{string.Join(",",arr1)}] sorted? {sorting.IsSorted(arr1)}");
            Console.WriteLine($"Is [{string.Join(",",arr2)}] sorted? {sorting.IsSorted(arr2)}");

            //Assignment Two
            var a = 3;
            var b = 7;
            var result = sorting.SwapTwoNumbers(a, b);

            Console.WriteLine($"Swap a:{a}, b:{b} => a:{result.Item1}, b:{result.Item2}");
        }
    }
}
