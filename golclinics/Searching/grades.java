public class grades {
    List<String> super_students (List <Grade> grades,List<Student> students){
        int minMark = 0;
        for (Grade grade: grades){
            if (grade.getGradeName()=="B"){
                minMark = grade.getStart();
            }
        }

        List<String> answer= new ArrayList();
        for (Student student: students){
            if (student.marks>=minMark){
                answer.add(student.getName());
            }
        }

        return answer;
    }
}
