using System;

namespace Binary_Assignment_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] listNumber = { 2, 7, 11, 15 };

            int target = 9;

            int count = 0;

            while (count != listNumber.Length - 1)
            {
                int last_index = listNumber.Length - 1;

                int first_index = 0;

                while (first_index <= last_index)
                {
                    int mid = first_index + (last_index - first_index) / 2;

                    if (listNumber[mid] == target)
                    {
                        mid = mid + 0;
                    }
                    else if (listNumber[mid] < target)
                    {
                        if (count != mid)
                        {
                            if (listNumber[count] + listNumber[mid] == target)
                            {
                                Console.Write($"[{ count }, { mid }] ");
                            }
                        }

                        first_index = mid + 1;
                    }
                    else
                    {
                        if (count != mid)
                        {
                            if (listNumber[count] + listNumber[mid] == target)
                            {
                                Console.Write($"[{ count }, { mid }] ");
                            }
                        }

                        last_index = mid - 1;
                    }
                }

                count++;
            }
        }
    }
}
