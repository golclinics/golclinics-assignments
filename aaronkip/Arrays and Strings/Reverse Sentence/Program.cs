using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reverse_Sentence
{
   class Program
    { 
        static void Main(string[] args)
        {
            char[] array1  = {'t','h','i','s',' ','i','s'};
            Array.ForEach(ReverseSentence(array1), Console.WriteLine);
        }
        static char[] ReverseSentence(char[] a){
           String sentence = new String(a);
           string[] s = sentence.Split(' ');
           int decreasingCount = s.Length ;
           for(var i = 0; i< decreasingCount ; i++ ){
               decreasingCount--;
               (s[i], s[decreasingCount]) = (s[decreasingCount],s[i]);
     
           }
           string reversedSentence = string.Join(' ', s);
           char[] combinedChar = reversedSentence.ToCharArray();
           return combinedChar;
           
        }
    }
}
