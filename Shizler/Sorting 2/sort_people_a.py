class Person:
    def __init__(self,name,age,location) -> None:
        self.name = name
        self.age = age
        self.location = location
    def __str__(self):
        return str.format("({},{},{})", self.name, self.age,self.location)

people = [
  Person("Dennis", 44, "Nairobi"),
  Person("Mary", 14, "Kisumu"),
  Person("John", 13, "kwale"),
  Person("Ruth", 24, "Mandera"),
  Person("Karen", 32, "Kakuma"),
  Person("Peter", 29, "Isiolo"),
  Person("Irene", 7, "nyeri"),
  Person("Mohamud", 21, "voi"),
]


def sort_people(people,compare_function):
    for p in range(1,len(people)):
        person = people[p]

        j = p - 1
        while j>=0 and compare_function(person, people[j]):
            people[j+1] = people[j]
            j-=1
        people[j+1] = person
    
    # to view the ordered objects
    for p in people:  
        print(p)

    return people


sort_people(people, lambda a,b: a.age < b.age) # sort by age
print()
sort_people(people, lambda a,b: a.location < b.location) # sort by location
print()
sort_people(people, lambda a,b: a.name < b.name) #sort by name

