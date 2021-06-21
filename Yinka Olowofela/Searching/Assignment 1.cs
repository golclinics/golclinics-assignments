using System;

namespace Assignment_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] listNumber = { 3, 3 };

            int target = 6;

            int count = 0;

            while(count != listNumber.Length - 1)
            {
                for (int i = 0; i < listNumber.Length; i++)
                {
                    if (count != i)
                    {
                        if (listNumber[count] + listNumber[i] == target)
                        {
                            Console.Write($"[{count}, {i}] ");
                        }
                    }
                }

                count++;
            }
        }
    }
}