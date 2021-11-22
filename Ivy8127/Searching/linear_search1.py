class Grade:
  def __init__(self, start, to, gradeName):
    self.start = start
    self.to = to
    self.gradeName = gradeName

grades = [
  Grade(90, 100, "A"),
  Grade(80, 89, "B"),
  Grade(70, 79, "C"),
  Grade(60, 69, "D"),
  Grade(0, 59, "E")
]
class Student:
  def __init__(self, name, marks):
    self.name = name
    self.marks = marks

students = [
  Student("Dennis", 44),
  Student("Ken", 90),
  Student("Derick", 32),
  Student("James", 67),
  Student("Joyce", 76),
  Student("Linet", 29),
  Student("Ben", 96),
  Student("Jane", 82)
]
#Implement a function named super_students that returns names of students
# who scored grades "A" and "B"
def super_students(grades,students):
    names = []
    count = 0
    for student in students:
        if (student.marks in range(grades[0].start,grades[0].to)) or (student.marks in range(grades[1].start,grades[1].to)):
            names.append(student.name)

    return names
print(super_students(grades,students))