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

''' 
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
'''

class Grade: 
  def __init__(self, start, to, gradeName): 
    self.start = start 
    self.to = to 
    self.gradeName = gradeName

  def grading(self, marks):
    if marks >= self.start and marks <= self.to:
      return self.gradeName
  
  def binaryGrading(self, marks):
    return

class Student: 
  def __init__(self, name, marks): 
    self.name = name 
    self.marks = marks

  def super_students(grades, students):
    res = []
    for student in students:   #n
      for grade in grades:   #m
        if grade.grading(student.marks) == 'A' or grade.grading(student.marks) == 'B':
          res.append(student.name)
    print(res)
    return res

  def binarySearch(grade, students):
    n = len(students)
    mid = (0 + n-1) // 2
    res = []
    for i in range(mid, n):
      if students[i].marks >= grade:
        res.append(students[i].name)
    return res

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
Student.binarySearch(grades, students)


"""