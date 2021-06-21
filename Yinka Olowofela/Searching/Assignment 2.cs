using System;

namespace Search_Assignment_2
{
    class Program
    {
        private static int count = 0;

        public int counting
        {
            get
            {
                return count;
            }
        }

        static void Main(string[] args)
        {
            Grade[] grades = 
            {
                new Grade(90, 100, 'A'),
                new Grade(80, 89, 'B'),
                new Grade(70, 79, 'C'),
                new Grade(60, 69, 'D'),
                new Grade(0, 59, 'E')
            };

            Student[] students =
            {
                new Student("Dennis", 44),
                new Student("Ken", 90),
                new Student("Derick", 32),
                new Student("James", 67),
                new Student("Joyce", 76),
                new Student("Linet", 29),
                new Student("Ben", 96),
                new Student("Jane", 82)
            };

            string[] list_super_student = new string[count];
            
            list_super_student = super_students(grades, students);

            for (int i = 0; i < count; i++)
            {
                Console.WriteLine($" {i + 1} { list_super_student[i] }");
            }
        }

        public static string[] super_students(Grade[] grades, Student[] students)
        {
            string[] list_student = new string[students.Length];

            for (int i = 0; i < students.Length; i++)
            {
                for (int j = 0; j < 2; j++)
                {
                    if(students[i].getMark >= grades[j].getStart && students[i].getMark <= grades[j].getTo)
                    {
                        list_student[count] = students[i].getName;

                        count++;
                    }
                }
            }

            return list_student;
        }
    }

    public class Grade
    {
        private int _start;

        private int _to;

        private char _gradeName;

        public Grade(int start, int to, char gradeName)
        {
            this._start = start;
            this._to = to;
            this._gradeName = gradeName;
        }

        public int getStart
        {
            get
            {
                return this._start;
            }
        }

        public int getTo
        {
            get
            {
                return this._to;
            }
        }

        public char getGradeName
        {
            get
            {
                return this._gradeName;
            }
        }
    }

    public class Student
    {
        private string _name;

        private int _marks;

        public Student(string name, int marks)
        {
            this._name = name;
            this._marks = marks;
        }

        public string getName
        {
            get
            {
                return this._name;
            }
        }

        public int getMark
        {
            get
            {
                return this._marks;
            }
        }
    }
}