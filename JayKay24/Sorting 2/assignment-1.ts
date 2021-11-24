import { Comparator, LessThan, GreaterThan } from "./comparator";
import { insertionSort } from "./insertion-sort";

export class Person {
  name: string;
  age: number;
  location: string;

  constructor(name: string, age: number, location: string) {
    this.name = name;
    this.age = age;
    this.location = location;
  }
}

const people = [
  new Person("Dennis", 44, "Nairobi"),
  new Person("Mary", 14, "Kisumu"),
  new Person("John", 13, "kwale"),
  new Person("Ruth", 24, "Mandera"),
  new Person("Karen", 32, "Kakuma"),
  new Person("Peter", 29, "Isiolo"),
  new Person("Irene", 7, "nyeri"),
  new Person("Mohamud", 21, "voi"),
];

/**
 * Sort the people based on age, location and name
 *
 * @param people - an array of Person objects
 * @returns a totally ordered set of objects
 */
function sort_people(
  people: Person[],
  prop: string,
  comparator: Comparator
): Person[] {
  return insertionSort(people, prop, comparator);
}

console.log(sort_people(people, "age", new LessThan()));
console.log(sort_people(people, "location", new GreaterThan()));
console.log(sort_people(people, "name", new LessThan()));
