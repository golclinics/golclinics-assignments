using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace Searching
{
    public class Student
    {
        public string name;

        public int marks;

        public Student(string name, int marks)
        {
            this.name = name;
            this.marks = marks;

        }


    }
    /// <summary>
    /// A class representing a subject Grade as below:
    /// <list type="params">
    /// <item>
    /// <description>start</description>
    /// </item>
    /// <item>
    /// <description>to</description>
    /// </item>
    /// </list>
    /// <param name="start">represent the lower bound of grade value</param>
    /// <param name="to">represent the higher bound range</param>
    /// <param name="gradename">char representation of grade on the range</param>
    /// </summary>

    public class Grade
    {
        static int start;

        static int to;

        static char gradename;

        public Grade(int start, int to, char gradename)
        {

            //this.start = start;
            //this.to = to;
            //this.gradename = gradename;

        }
        
    }


    class Program
    {
        public String super_student(Student[] students, Grade[] grades)
        {
            

            for(int i=0; i < students.Length; i++)
            {
                if (grading(students[i].marks) == 'A' || grading(students[i].marks) == 'B')
                {
                    Console.WriteLine( students[i].name);
                }
                
            }

            return "Not Found";
        }
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
                        return new KeyValuePair<int, int>(i, j);
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

        public static char grading(int marks)
        {

            if (marks >= 0 && marks < 59)
            {
                return 'E';

            }
            else if (marks >= 60 && marks <= 69)
            {
                return 'D';

            }
            else if (marks >= 70 && marks <= 79)
            {
                return 'C';
            }
            else if (marks >= 80 && marks <= 89)
            {
                return 'B';
            }
            else if (marks >= 90 && marks <= 100)
            {
                return 'A';
            }

            return 'Z';
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

            Console.WriteLine(" --------------------------------------------------------------------------------------------------------- \n");



            Grade[] grades = new Grade[] { new Grade(90, 100, 'A'), new Grade(80, 89, 'B'), new Grade(70, 79, 'C'), new Grade(60, 69, 'D'), new Grade(0, 59, 'E') };

            Student[] students = new Student[] { new Student("Dennis", 44), new Student("Ken", 90), new Student("Derick", 32), new Student("James", 67), new Student("Joyce", 76),
                                    new Student("Linet", 29),new Student("Ben", 96),new Student("Jane", 82)};


            Program prg = new Program();

            string res = prg.super_student(students, grades);

            Console.WriteLine(res);

            

            Console.ReadLine();
        }
    }
}