using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Searching
{

    class Program
    {
        /*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.//
         Assumption : You may assume that each input would have exactly one solution, and you may not use the same element twice.

            You can return the answer in any order.
         */
        public static KeyValuePair<int, int> double_sum(int[] arr, int target)
        {
            int[] indexs = arr;

            for (int i = 0; i < arr.Length; i++)
            {
                for (int j = 1; j < arr.Length - 1; j++)
                {
                    if ((indexs[i] + indexs[j] == target) || target == indexs[i])
                    { 
                        int index1 = indexs[i];

                        int index2 = indexs[j];

                        return new KeyValuePair<int, int>(index1, index2);
                    }

                }
            }

            return new KeyValuePair<int, int>(target, 0);
        }

        /*Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.//
         NB : Ignoring Assumption above.
         */
        public static List<KeyValuePair<int, int>> double_sum2(int[] arr, int target)
        {
            Dictionary<int, int> dict = new Dictionary<int, int>();

            for (int i = 0; i < arr.Length; i++)
            {
                dict.Add(arr[i], i);
            }

            List<int> keys = dict.Keys.ToList();

            List<KeyValuePair<int, int>> pairs = new List<KeyValuePair<int, int>>();

            foreach (var x in keys)
            {
                if (!dict.ContainsKey(x))
                {
                    continue;
                }

                int difference = target - x;
                if (dict.ContainsKey(difference))
                {
                    pairs.Add(new KeyValuePair<int, int>(dict[x], dict[difference]));
                    dict.Remove(x);
                    dict.Remove(difference);
                }
            }

            return pairs;
        }
        
        static void Main(string[] args)
        {
            Console.WriteLine(" --------------------------------------------------------------------------------------------------------- \n");

            Console.WriteLine("Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target \n");

            Console.WriteLine("Assumption : You may assume that each input would have exactly one solution, and you may not use the same element twice. \n");

            int[] my_arr = { 6, 8, 4, 5, 9 };

            Console.WriteLine("Array of Ints : " + string.Join(",", my_arr));

            var pairs = double_sum2(my_arr, 13);

            foreach (var pair in pairs)
            {
                Console.WriteLine("position of 1st is :  " + pair.Key + "  postion of 2nd is :  " + pair.Value);
            }

            Console.WriteLine(" --------------------------------------------------------------------------------------------------------- \n");

            Console.WriteLine("Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target \n");

            var pairs1 = double_sum(my_arr, 13);

            Console.WriteLine(pairs1);

            Console.ReadLine();
        }
    }
}
