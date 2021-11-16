/*
Implement a hash function hashObject that takes in a Student object S with the following fields:
class Student:
  string name
  int age
  long marks
and computes a hash value V for the object
*/
public class hashobj {
    public static void main(String[] args) {
        Student s = new Student("Jacob", 20, 100);
        int hash = 0;
        for (int i = 0; i < s.name.length(); i++) {
            hash = hash + (int) s.name.charAt(i);
        }
        hash = hash + s.age;
        hash = hash + (int) s.marks;
        System.out.println(hash);
    }
    
}
