using System.Collections.Generic;
using System;

namespace String_Manipulations
{
    class Program
    {
        /* Given two strings, a and b , that may or may not be of the same length, 
         * determine the minimum number of character deletions required to make a and b anagrams. 
         * 
         * Any characters can be deleted from either of the strings.*/

        public static int makeAnagram(string a , string b)
        {
            int deletions =  0 ;

            Dictionary <char, int> dict = new Dictionary<char, int>();

            foreach(var chara in a)
            {
                if (dict.ContainsKey(chara))
                {
                    dict[chara]++;
                }
                else
                {
                    dict.Add(chara, 1);
                }
            }

            foreach(var charb in b)
            {
                if(dict.ContainsKey(charb))
                {
                    dict[charb]--;
                }
                else
                {
                    deletions++;
                }
            }

            foreach (var chara in dict)
            {

                deletions += Math.Abs(chara.Value);

            }

            return deletions;





        }
        /* Implementing above solution using an array */
        public static int makeAnagramb(string a, string b)
        {

            int[] charValues = new int[26];

            foreach (char c in a)
            {
                int cVal = (int)c - 97;

                charValues[cVal]++;

            }
            foreach (char c in b)
            {
                int cVal = (int)c - 97;

                charValues[cVal]--;
            }

            int deletions = 0;

            foreach (int i in charValues)
            {
                deletions += Math.Abs(i);
            }

            return deletions;

        }
        static void Main(string[] args)
        {

            string a = "jxwtrhvujlmrpdoqbisbwhmgpmeoke";

            string b = "fcrxzwscanmligyxyvym";



            Console.WriteLine("String A: "+ a);

            Console.WriteLine("String B: " + b);



            Console.WriteLine("Number of deletions required to make string A and string B an anagram are : " + makeAnagram(a,b) + "\n");

            Console.WriteLine("Number of deletions required to make string A and string B an anagram are : " + makeAnagramb(a, b));


        }
    }
}
