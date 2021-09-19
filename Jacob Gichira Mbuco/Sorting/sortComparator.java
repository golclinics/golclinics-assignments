import java.util.Collection;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class sortComparator {
    //order by age , location , name
    //method 1
    List<Person> sortJava8(List<Person> persons){
        Collections.sort(persons,(a,b)->(a.name).compareTo(b.name));
        return persons;
    }
    //method 2 inner class
    List<Person> sortComparatorEx(List<Person> persons){
        Collections.sort(persons, new Comparator<Person> (){
           //The method sort(List<Person>, new Comparator<Person>(){}) is undefined for the type CollectionJava(67108964)

            @Override
            public int compare(Person x, Person y) {
                if(x.age!=y.age){
                    return (x.age-y.age);
                }else if(!x.location.equals(y.location)){
                    return (x.location.compareTo(y.location));
                }else{
                    return (x.name.compareTo(y.name));
                }
            }

        });
        return persons;
    }
}
// 1 -> 2 -> 3
// 3 -> 2 -> 1
class Person{
    public String name, location;
    public int age;
    public Person(String name,int age,String location){
        this.name = name;
        this.age = age;
        this.location = location;
    }
}
