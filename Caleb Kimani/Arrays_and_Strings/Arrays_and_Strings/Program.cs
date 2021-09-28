using System;

namespace Arrays_Gol
{
    class Program
    {
        private static void swap(int[] arr)
        {

            int i = 0;
            int j = arr.Length - 1;
            while (i < j)
            {
                var temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }

        }

        private static string swapsen(char[] input)
        {
            
            for (int i = 0; i < input.Length / 2; i++)
            {
                //reverse the expression
                char tmp = input[i];
                input[i] = input[input.Length - i - 1];
                input[input.Length - i - 1] = tmp;
            }
            for (int j = 0, start = 0, end = 0; j <= input.Length; j++)
            {
                if (j == input.Length || input[j] == ' ')
                {
                    end = j - 1;
                    for (; start < end;)
                    {
                        char tmp = input[start];
                        input[start] = input[end];
                        input[end] = tmp;
                        start++;
                        end--;
                    }
                    start = j + 1;
                }
            }
            return new string(input);
        }

        /* You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. 
         * You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order. */
        static int minimumSwaps(int[] arr)
        {
            int count = 0;

            int i = 0;

            while (i < arr.Length)
            {
                int index = arr[i] - 1;

                if (arr[i] != arr[index])
                {

                    var temp = arr[index];
                    arr[index] = arr[i];
                    arr[i] = temp;
                    count++;
                }
                else
                {
                    i++;
                }
            }
            return count;


        }

        /* Functions counts the number of times the input number n can be divided by 2 before it reaches one or less. */
        static int count_div_2(long n)
        {
            int num = 0;

            while (n != 0)
            {
                n = n / 2;
                num++;

            }

            return num;
        }
        public static void Main()
        {
            
            long num = 60;

            Console.WriteLine("///////////////////////////////////////////////////////// \n");

            Console.WriteLine("Functions counts the number of times the input number : " + num +" can be divided by 2 before it reaches one or less.");

            Console.WriteLine("Number of"
                          + " times : " + count_div_2(num));

            Console.WriteLine("///////////////////////////////////////////////////////// \n");

            string word = "This is a Boy";

            Console.WriteLine("Function that swaps sentence below without swapping the words : "+word);

            char[] str2 = word.ToCharArray();

            string new_str = swapsen(str2);

            Console.WriteLine(new_str);

            Console.WriteLine("///////////////////////////////////////////////////////// \n");

            int[] array = new int[]{ 7 , 1 , 3 , 2, 4, 5, 6 };

            Console.WriteLine("Unordered array is : " + string.Join(",", array));

            int count = minimumSwaps(array);

            Console.WriteLine("number of swaps to sort the array: " + count);

            Console.ReadLine();


            
        }

    }

}
