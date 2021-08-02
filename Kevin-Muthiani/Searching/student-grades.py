# Implement a function named super_students that returns names of
# students who scored grades "A" and "B"

from typing import List


class Grade:
    def __init__(self, start, to, grade_name):
        self.start = start
        self.to = to
        self.grade_name = grade_name


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


def super_students(students: List[Student], grades: List[Grade]) -> List[str]:

    def has_required_grade(student: Student, valid_grades: List[Grade]) -> bool:
        """ Helper function to check if student has a valid grade """

        for grade in valid_grades:
            if (student.marks >= grade.start) and (student.marks <= grade.to):
                return True
        return False


    valid_grades = [ grade for grade in grades if (grade.grade_name in ["A", "B"] )]
    valid_students = []

    for student in students:
        if has_required_grade(student, valid_grades):
            valid_students.append(student)

    return valid_students


# Test
grades = [
  Grade(90, 100, "A"),
  Grade(80, 89, "B"),
  Grade(70, 79, "C"),
  Grade(60, 69, "D"),
  Grade(0, 59, "E")
]


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

super_students_list = super_students(students, grades)

for student in super_students_list:
    print(student.name, " - ", student.marks)