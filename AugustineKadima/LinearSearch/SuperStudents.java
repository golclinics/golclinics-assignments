import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class SuperStudents {

    public static ArrayList<String> super_students(ArrayList<Grades> mGrades, ArrayList<Students> mStudents){

        List<Grades> grades = mGrades;
        List<Students> students = mStudents;

        ArrayList<String> names = new ArrayList<>();

        HashMap<Integer, Character> gradesAAndB = new HashMap<>();
        int n = grades.size() - 1;
        int m = students.size() -1;
        for(int i = 0; i <= n; i++){
            if(grades.get(i).getStart() >= 80){
                gradesAAndB.put(grades.get(i).getStart(), grades.get(i).getGrade());
            }
        }

        for(int i = 0; i <= m; i++){
            if(students.get(i).getMarks() >= 80 && students.get(i).getMarks() < 90){
                names.add("Name: "+students.get(i).getName() + " " + gradesAAndB.get(80));
            }else if(students.get(i).getMarks() >= 90 && students.get(i).getMarks() <= 100){
                names.add( "Name: "+students.get(i).getName() + " " + gradesAAndB.get(90));
            }
        }

        for(String name:names){
            System.out.println(name);
        }

        return names;
    }

    public static void main(String[] args) {

        ArrayList<Grades> grades = new ArrayList<>();
        grades.add(new Grades(90, 100, 'A'));
        grades.add(new Grades(80, 89, 'B'));
        grades.add(new Grades(70, 79, 'C'));
        grades.add(new Grades(60, 69, 'D'));
        grades.add(new Grades(0, 59, 'E'));

        ArrayList<Students> students = new ArrayList<>();
        students.add(new Students("Dennis", 44));
        students.add(new Students("Ken", 90));
        students.add(new Students("Derick", 32));
        students.add(new Students("James", 67));
        students.add(new Students("Joyce", 76));
        students.add(new Students("Linet", 29));
        students.add(new Students("Ben", 96));
        students.add(new Students("Jane", 82));

        SuperStudents.super_students(grades, students);
    }
}

class Grades{
    private int start;
    private int to;
    private char grade;

    public Grades(int start, int to, char grade) {
        this.start = start;
        this.to = to;
        this.grade = grade;
    }

    public int getStart() {
        return start;
    }

    public void setStart(int start) {
        this.start = start;
    }

    public int getTo() {
        return to;
    }

    public void setTo(int to) {
        this.to = to;
    }

    public char getGrade() {
        return grade;
    }

    public void setGrade(char grade) {
        this.grade = grade;
    }
}

class Students{
    private String name;
    private int marks;

    public Students(String name, int marks) {
        this.name = name;
        this.marks = marks;
    }

    public Students(){}
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getMarks() {
        return marks;
    }

    public void setMarks(int marks) {
        this.marks = marks;
    }
}