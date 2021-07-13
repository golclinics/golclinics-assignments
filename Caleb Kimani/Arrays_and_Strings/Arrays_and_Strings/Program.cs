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

        private static string swapsen(char[] input1)
        {
            char[] input = "dog world car life".ToCharArray();
            for (int i = 0; i < input.Length / 2; i++)
            {//reverse the expression
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

        //hackerank implementation
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
            long num = 1152921504606846976;

            Console.WriteLine("Number of"
                          + " digits : " + count_div_2(num));

            Console.ReadLine();


            /*
             * 
            int[] array = { 2, 4, 6, 8 };

            string word = "This is a Boy";

            swap(array);

            char[] str2 = word.ToCharArray();

            string new_str = swapsen(str2);

            int num2 = count_div_2(100);

            Console.WriteLine(String.Join(',', array));

            Console.WriteLine(new_str);

            Console.WriteLine(num2);

            Console.ReadLine(); */

            //Console.WriteLine(count_div_2(100));
        }

    }

}
