using System.Collections.Generic;
using System.Linq;

namespace Searching
{
  public class StudentMarks
  {
    public List<Grade> grades = new List<Grade>
    {
      new Grade(90, 100, "A"),
      new Grade(80, 89, "B"),
      new Grade(70, 79, "C"),
      new Grade(60, 69, "D"),
      new Grade(0, 59, "E")
    };

    public List<Student> students = new List<Student>()
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
    
    public IEnumerable<string> GetSuperStudents()
    {
      //Super students have scored B and above
      var minScore = grades.Find(g => g.GradeName == "B").Start;
      return students.Where(s => s.Marks >= minScore).Select(s => s.Name);
    }
  }

  public class Grade
  {
    public string GradeName { get; set;}
    public int Start { get; set;}
    public int To { get; set;}
    public Grade(int start, int to, string gradeName)
    {
      GradeName = gradeName;
      Start = start;
      To = to;
    }
  }

  public class Student
  {
    public string Name { get; set;}
    public int Marks { get; set;}
    public Student(string name, int marks)
    {
      Name = name;
      Marks = marks;
    }
  }
}
