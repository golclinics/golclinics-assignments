using System;

namespace Searching
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            var twoIndices = new TwoIndices();
            var nums = new int[]{2,7,11,15};
            var target = 9;
            var indices = twoIndices.AddUpToTarget(nums, target);

            // Console.WriteLine($"Array: [{string.Join(",", nums)}], targetSum: {target}, indices: [{string.Join(",", indices)}]");

            var studentMarks = new StudentMarks();
            var superStudents = studentMarks.GetSuperStudents();
            foreach(var s in superStudents)
            {
              Console.WriteLine($"{s.Name}, {s.Marks}");
            }
        }
    }
}
