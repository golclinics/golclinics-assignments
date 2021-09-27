class PersonComparator:
    @staticmethod
    def compare(person_1, person_2):
        """
        return 0 if person_1 == person_2
        return >0 if person_1 > person_2
        return <0 if person_1 < person_2
        """
        raise NotImplementedError


class PersonComparable:
    def compare_to(self, person_2, comparator):
        return comparator.compare(self, person_2)


class PersonAgeComparator(PersonComparator):
    @staticmethod
    def compare(person_1, person_2):
        if person_1.age == person_2.age:
            return 0
        elif person_1.age > person_2.age:
            return 1
        else:
            return -1


class PersonLocationComparator(PersonComparator):
    @staticmethod
    def compare(person_1, person_2):
        if person_1.location.lower() == person_2.location.lower():
            return 0
        elif person_1.location.lower() > person_2.location.lower():
            return 1
        else:
            return -1


class PersonNameComparator(PersonComparator):
    @staticmethod
    def compare(person_1, person_2):
        if person_1.name.lower() == person_2.name.lower():
            return 0
        elif person_1.name.lower() > person_2.name.lower():
            return 1
        else:
            return -1


class Person(PersonComparable):
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location


def swap_array_elements(array_list, i, j):
    """
    Helper function to swap elements at index i and j in array_list (in place)
    """
    temp = array_list[i]
    array_list[i] = array_list[j]
    array_list[j] = temp


def sort_people_insertion(people, comparator):
    """ Sort people list using insertion sort algorithm """

    for i in range(1, len(people)):
        j = i - 1
        key_person = people[i]

        while (j >= 0) and (key_person.compare_to(people[j], comparator) < 0):
            people[j+1] = people[j]
            j -= 1

        people[j+1] = key_person

    return people


def sort_people_bubble(people, comparator):
    """ Sort people list using bubble sort algorithm (adaptable approach) """
    is_sorted = False
    n = 1 # Continously decrement number of iterations in each outer loop pass

    while (not is_sorted):
        is_sorted = True

        for i in range(len(people) - n):
            if people[i].compare_to(people[i+1], comparator) > 0:
                swap_array_elements(people, i, i+1)
                is_sorted = False

        n += 1

    return people


def sort_people_selection(people, comparator):
    """ Sort people list using selection sort algorithm """

    for i in range(len(people)):
        min_person_key = i

        for j in range(i, len(people)):
            if people[min_person_key].compare_to(people[j], comparator) > 0:
                min_person_key = j

        if min_person_key != i:
            swap_array_elements(people, i, min_person_key)

    return people


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

#  Tests
print("Insertion Sort ...")
sort_people_insertion(people, PersonNameComparator)
print([ person.name for person in people ])
sort_people_insertion(people, PersonAgeComparator)
print([ person.age for person in people ])
sort_people_insertion(people, PersonLocationComparator)
print([ person.location for person in people ])
print("")

print("Adaptive Bubbe Sort ...")
sort_people_bubble(people, PersonNameComparator)
print([ person.name for person in people ])
sort_people_bubble(people, PersonAgeComparator)
print([ person.age for person in people ])
sort_people_bubble(people, PersonLocationComparator)
print([ person.location for person in people ])
print("")

print("Selection Sort ...")
sort_people_selection(people, PersonNameComparator)
print([ person.name for person in people ])
sort_people_selection(people, PersonAgeComparator)
print([ person.age for person in people ])
sort_people_selection(people, PersonLocationComparator)
print([ person.location for person in people ])
print("")