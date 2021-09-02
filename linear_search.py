#ASSIGNMENT ONE
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9 Output: [0,1] Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6 Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6 Output: [0,1]

nums = [2,7,11,15]
target = 9
lst = []
for i in nums:
    for j in nums:
        if nums.index(i) != nums.index(j):
            n = i + j
            if n == target:
                lst.append([nums.index(i), nums.index(j)])         
print(lst[0])


#ASSIGNMENT TWO

Given:
A class representing a subject Grade as below:
class Grade: def __init__(self, start, to, gradeName): self.start = start self.to = to self.gradeName = gradeName
A List of available grades below:
grades = [ Grade(90, 100, "A"), Grade(80, 89, "B"), Grade(70, 79, "C"), Grade(60, 69, "D"), Grade(0, 59, "E") ]
A class representing student marks as below:
class Student: def __init__(self, name, marks): self.name = name self.marks = marks
A list of students marks a below:
students = [ Student("Dennis", 44), Student("Ken", 90), Student("Derick", 32), Student("James", 67), Student("Joyce", 76), Student("Linet", 29), Student("Ben", 96), Student("Jane", 82) ]
Implement a function named super_students that returns names of students who scored grades "A" and "B" i.e

def super_students(grades, students): return "names of students who score grades A and B"


class Grade: 
  def __init__(self, start, to, gradeName): 
    self.start = start 
    self.to = to 
    self.gradeName = gradeName

  def gradesystem(self, marks):
    if marks >= self.start and marks <= self.to:
      return self.gradeName
  
  def binaryGrading(self, marks):
    return

class Student: 
  def __init__(self, name, marks): 
    self.name = name 
    self.marks = marks

  def super_students(grades, students):
    results = []
    for student in students:
      for grade in grades:
        if grade.gradesystem(student.marks) == 'A' or grade.gradesystem(student.marks) == 'B':
          results.append(student.name)
    print(results)
    return results

grades = [ 
    Grade(90, 100, "A"), 
    Grade(80, 89, "B"), 
    Grade(70, 79, "C"), 
    Grade(60, 69, "D"), 
    Grade(0, 59, "E") ]

students = [ 
  Student("Linet", 29),
  Student("Derick", 32),
  Student("Dennis", 44), 
  Student("James", 67),
  Student("Joyce", 76),
  Student("Jane", 82),
  Student("Ken", 90), 
  Student("Ben", 96) 
   ]

Student.super_students(grades, students)
"""



#Iterative - using loops.

def Binarysearch(target, array, low, high):
  
  while low <= high:
    mid = low + (high - low)//2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      high -= mid
    else:
      low += mid
  return -1

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(Binarysearch(10, array, 0, len(array)-1))

#recursive

def BinarySearch(key, list, low, high):
  if low > high:
    return -1
  else:
    mid = low + (high - low)//2
    if list[mid] == key:
      return mid
    elif list[mid] > key:
      return BinarySearch(key, list, low, mid-1)
    else:
      return BinarySearch(key, list, mid+1, high)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(BinarySearch(3, list, 0, len(list)-1))



def twoNum(arr, target):
    numToIndex = map(lambda x: x, arr)

    n = len(arr)
    newArr = []

    for i in range(n):
        complement = target - arr[i]
        if complement in numToIndex:
            newArr.append(complement)
    return newArr

print(twoNum([8, 1, 2, 7, 11, 15, 22, 5, 4, ], 9))

#ASSIGNMENT TWO

"""

def twosum(nums=(6, 7, 11, 15, 3, 6, 5, 3), target=6):
    lookup = dict(((v, i) for i, v in enumerate(nums)))
    return next(( (i+1, lookup.get(target-v)+1) 
            for i, v in enumerate(nums) 
                if lookup.get(target-v, i) != i), None)
"""











"""

namespace Searching
{

    class Grade
    public class Student
    {
        int start;
        public string name;

        int to;
        public int marks;

        char gradename;
        public Grade(int start, int to, char gradename)
        public Student(string name, int marks)
        {
            this.start = start;
            this.to = to;
            this.gradename = gradename;
            this.name = name;
            this.marks = marks;

        }
    }

    class Student

    }
   
    public class Grade
    {
        string name;
        static int start;

        int marks;
        public Student(string name, int marks)
        static int to;

        static char gradename;

        public Grade(int start, int to, char gradename)
        {
            this.name = name;

            this.marks = marks;
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
@@ -96,8 +131,37 @@ class Program
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
@@ -125,15 +189,25 @@ static void Main(string[] args)

            Console.WriteLine(pairs1);

            Grade mygrades = new Grade(90, 100 ,'A');
            Grade mygrades2 = new Grade(80, 89, 'B');
            Grade mygrades3 = new Grade(70, 79, 'C');
            Grade mygrades4 = new Grade(60, 69, 'D');
            Grade mygrades5 = new Grade(0, 59, 'E');
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
}
"""