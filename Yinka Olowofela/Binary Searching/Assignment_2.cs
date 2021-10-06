using System;

namespace Binary_Assignment_2
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
                new Student("Linet", 29),
                new Student("Derick", 32),
                new Student("Dennis", 44),
                new Student("James", 67),
                new Student("Joyce", 76),
                new Student("Jane", 82),
                new Student("Ken", 90),
                new Student("Ben", 96)
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

            int findTarget = binary_iterative_search(students, grades[1].getStart);

            for (int i = findTarget; i < students.Length; i++)
            {
                list_student[count] = students[i].getName;

                count++;
            }

            return list_student;
        }

        public static int get_mid(int first_index, int last_index)
        {
            return first_index + (last_index - first_index) / 2;
        }

        public static int binary_iterative_search(Student[] arrayNumber, int target)
        {
            int last_index = arrayNumber.Length - 1;
            int first_index = 0;

            while (first_index <= last_index)
            {
                int mid = get_mid(first_index, last_index);

                if (arrayNumber[mid].getMark >= target)
                {
                    return mid;
                }
                else if (target < arrayNumber[mid].getMark)
                {
                    last_index = mid - 1;
                }
                else
                {
                    first_index = mid + 1;
                }
            }

            return -1;
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