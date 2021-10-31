class Grade {
  start: number;
  to: number;
  gradeName: string;

  constructor(start: number, to: number, gradeName: string) {
    this.start = start;
    this.to = to;
    this.gradeName = gradeName;
  }
}

class Student {
  name: string;
  marks: number;

  constructor(name: string, marks: number) {
    this.name = name;
    this.marks = marks;
  }
}

/**
 * Build and return lower and upper bounds of grades "A" to "B";
 *
 * @param grades - Grades to use to establish a valid range
 * @returns Tuple containing lower and upper bounds of grade A to B
 */
function build_grade_range_A_to_B(grades: Grade[]): [number, number] {
  let lower_bound = 0,
    upper_bound = 0;

  for (const grade of grades) {
    if (grade.gradeName === "A") {
      upper_bound = grade.to;
    } else if (grade.gradeName === "B") {
      lower_bound = grade.start;
    }
  }

  return [lower_bound, upper_bound];
}

/**
 * Return names of students who scored grades "A" and "B"
 *
 * @param grades - An array of grades each containing it's letter and it's lower and upper bound
 * @param students - An array of students
 * @returns Names of students who scored B and above
 */
function super_students(grades: Grade[], students: Student[]): string[] {
  const passed_students: string[] = [];
  const [lower_bound, upper_bound] = build_grade_range_A_to_B(grades);

  for (const student of students) {
    if (student.marks >= lower_bound && student.marks <= upper_bound) {
      passed_students.push(student.name);
    }
  }

  return passed_students;
}

const grades = [
  new Grade(90, 100, "A"),
  new Grade(80, 90, "B"),
  new Grade(70, 79, "C"),
  new Grade(60, 69, "D"),
  new Grade(0, 59, "E"),
];

const students = [
  new Student("Dennis", 44),
  new Student("Ken", 90),
  new Student("Derick", 32),
  new Student("James", 67),
  new Student("Joyce", 76),
  new Student("Linet", 29),
  new Student("Ben", 96),
  new Student("Jane", 82),
];
