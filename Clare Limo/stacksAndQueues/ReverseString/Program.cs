using System;
using System.Collections.Generic;
using System.Text;

namespace ReverseString
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(ReversedStringStack("world"));
        }
        
        //Write a program that reads a String and reverses the String using Stack Push and Pop operations
        public static string ReversedStringStack(string s){
            var charArr = s.ToCharArray();
            int n = charArr.Length;
            var st = new Stack<char>();

            for(int i=0;i<n;i++){
                st.Push(charArr[i]);
            }

            for (int i = 0; i <n; i++)
            {
                charArr[i] = st.Pop();
            }

            s = new string(charArr);

            return s;
        }
    }
}
