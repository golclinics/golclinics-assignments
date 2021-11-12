public class SortComparable {

}

class PersonCompare implements Comparable<Person> {
    public String name, location;
    public int age;

    public PersonCompare(String name,int age,String location){
        this.name = name;
        this.age = age;
        this.location = location;
    }

    @Override
    public int compareTo(Person o) {
        if(age != o.age){
            return age-o.age;
        }else if(!location.equals(o.location)){
            return location.compareTo(o.location);
        }else{
            return name.compareTo(o.name);
        }
    }
}
