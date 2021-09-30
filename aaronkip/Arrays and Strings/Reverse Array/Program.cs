using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Reverse_Array
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] array1  = {1,2,3,4,5};
            Array.ForEach(ReverseArray(array1), Console.WriteLine);
        }
        static int[] ReverseArray(int[] a){
           var reverseCounter = a.Length;
           for(var i = 0; i < reverseCounter ; i++){
               reverseCounter--;
               (a[i], a[reverseCounter]) = (a[reverseCounter], a[i]);
           }
           return a;
        }
    }
}
