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

# Time - O(m), Space - O(1); Where m = number of super grades
def has_super_grade(student: Student, super_grades: List[Grade]) -> bool:
    """ Helper function to check if student has a super grade """

    for grade in super_grades:
        if (student.marks >= grade.start) and (student.marks <= grade.to):
            return True
    return False


# Time - O(m*log(n)), Space - O(log(n)); Where m = size of super_grades & n = size of students
def last_super_student_index(students, super_grades, first, last):
    """
    Helper function that iteratively determines index of last student that had a super grade
    :param students: list if students sorted in ascending order by marks
    :param super_grades: list of valid grades for a student to be deemed a super student
    :param first: first index to consider
    :param last: last index to consider
    :return: index of last (from right hand side) student with super grade or -1 if none
    """
    minimum = -1

    if (first > last):
        return minimum

    mid = first + ((last - first) // 2)
    mid_student = students[mid]

    if has_super_grade(mid_student, super_grades):
        # All students on right side (including middle one) have super grades.
        # Record current index as minimum and check if there are others on left side
        minimum = mid
        last = mid - 1
    else:
        # All students on left side (including middle one) lack super grades.
        # Check the right side
        first = mid + 1

    new_minimum = last_super_student_index(students, super_grades, first, last)

    return new_minimum if (new_minimum != -1) else minimum


# Time - O(m + n+ m*log(n)), Space - O(m + n + log(n)); Where m = size of grades & n = size of students
def super_students(students: List[Student], grades: List[Grade]) -> List[str]:
    first_index = 0
    last_index = len(students) - 1
    super_grades = [ grade for grade in grades if (grade.grade_name in ["A", "B"] )]

    minimum_index = last_super_student_index(students, super_grades, first_index, last_index)

    if minimum_index >= 0:
        return [ student.name for student in students[minimum_index:] ]
    else:
        # No student passed
        return []


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

# Sort students by marks in ascending order
sorted_students = sorted(students, key=lambda student: student.marks)

print(super_students(sorted_students, grades))