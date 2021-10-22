using System;

namespace Stacks
{
    class Program
    {
        static void Main(string[] args)
        {
            var b0 = "()";
            var b1 = "()[]{}";
            var b2 = "(]";
            var b3 = "([)]";
            var b4 = "{[]}";
            Console.WriteLine($"is {b0} valid? : {StackExercises.IsValid(b0)}");
            Console.WriteLine($"is {b1} valid? : {StackExercises.IsValid(b1)}");
            Console.WriteLine($"is {b2} valid? : {StackExercises.IsValid(b2)}");
            Console.WriteLine($"is {b3} valid? : {StackExercises.IsValid(b3)}");
            Console.WriteLine($"is {b4} valid? : {StackExercises.IsValid(b4)}");
        }


    }
}
