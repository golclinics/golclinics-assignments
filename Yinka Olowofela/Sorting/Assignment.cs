using System;

namespace Sorting_Assignment
{
    class Program
    {
        static void Main(string[] args)
        {
            Person[] people =
            {
                new Person("Dennis", 44, "Nairobi"),
                new Person("Mary", 14, "Kisumu"),
                new Person("John", 13, "kwale"),
                new Person("Ruth", 24, "Mandera"),
                new Person("Karen", 32, "Kakuma"),
                new Person("Peter", 29, "Isiolo"),
                new Person("Irene", 7, "nyeri"),
                new Person("Mohamud", 21, "voi"),
            };

            Console.WriteLine("SELECTION SORTING FOR AGE");
            Person[] selection_result_age = selection_sort_age(people);
            for (int i = 0; i < selection_result_age.Length; i++)
            {
                Console.WriteLine($"Name: { selection_result_age[i].getName }, Age: { selection_result_age[i].getAge }, Location: { selection_result_age[i].getLocation }");
            }


            Console.WriteLine("\n\nINSERTION SORTING FOR AGE");
            Person[] Insertion_result_age = selection_sort_age(people);
            for (int i = 0; i < Insertion_result_age.Length; i++)
            {
                Console.WriteLine($"Name: { Insertion_result_age[i].getName }, Age: { Insertion_result_age[i].getAge }, Location: { Insertion_result_age[i].getLocation }");
            }


            Console.WriteLine("\n\nSELECTION SORTING FOR NAME");
            Person[] selection_result_name = selection_sort_name(people);
            for (int i = 0; i < selection_result_name.Length; i++)
            {
                Console.WriteLine($"Name: { selection_result_name[i].getName }, Age: { selection_result_name[i].getAge }, Location: { selection_result_name[i].getLocation }");
            }


            Console.WriteLine("\n\nINSERTION SORTING FOR NAME");
            Person[] insertion_result_name = insertion_sort_name(people);
            for (int i = 0; i < insertion_result_name.Length; i++)
            {
                Console.WriteLine($"Name: { insertion_result_name[i].getName }, Age: { insertion_result_name[i].getAge }, Location: { insertion_result_name[i].getLocation }");
            }


            Console.WriteLine("\n\nSELECTION SORTING FOR LOCATION");
            Person[] selection_result_location = selection_sort_location(people);
            for (int i = 0; i < selection_result_location.Length; i++)
            {
                Console.WriteLine($"Name: { selection_result_location[i].getName }, Age: { selection_result_location[i].getAge }, Location: { selection_result_location[i].getLocation }");
            }


            Console.WriteLine("\n\nINSERTION SORTING FOR LOCATION");
            Person[] insertion_result_location = insertion_sort_location(people);
            for (int i = 0; i < insertion_result_location.Length; i++)
            {
                Console.WriteLine($"Name: { insertion_result_location[i].getName }, Age: { insertion_result_location[i].getAge }, Location: { insertion_result_location[i].getLocation }");
            }
        }

        public static Person[] swap(int i, int j, Person[] person = null)
        {
            Person temp = person[i];
            person[i] = person[j];
            person[j] = temp;

            return person;
        }

        public static Person[] selection_sort_age(Person[] person = null)
        {
            for (int i = 0; i < person.Length; i++)
            {
                for (int j = i + 1; j < person.Length; j++)
                {
                    if (person[j].getAge < person[i].getAge)
                    {
                        swap(i, j, person);
                    }
                }
            }

            return person;
        }

        public static Person[] insertion_sort_age(Person[] person = null)
        {
            int value, flag;

            for (int i = 0; i < person.Length; i++)
            {
                value = person[i].getAge;

                flag = 0;

                for (int j = i - 1; j >= 0 && flag != 1;)
                {
                    if (value < person[j].getAge)
                    {
                        person[j + 1].getAge = person[j].getAge;

                        j--;

                        person[j + 1].getAge = value;
                    }
                    else
                    {
                        flag = 1;
                    }
                }
            }

            return person;
        }

        public static Person[] selection_sort_name(Person[] person = null)
        {
            for (int i = 0; i < person.Length; i++)
            {
                for (int j = i + 1; j < person.Length; j++)
                {
                    if (string.Compare(person[j].getName, person[i].getName) == -1)
                    {
                        swap(i, j, person);
                    }
                }
            }

            return person;
        }
        
        public static Person[] insertion_sort_name(Person[] person = null)
        {
            Person value;
            int flag;

            for (int i = 0; i < person.Length; i++)
            {
                value = person[i];

                flag = 0;

                for (int j = i - 1; j >= 0 && flag != 1;)
                {
                    if (string.Compare(value.getName, person[j].getName) == -1)
                    {
                        person[j + 1] = person[j];

                        j--;

                        person[j + 1] = value;
                    }
                    else
                    {
                        flag = 1;
                    }
                }
            }

            return person;
        }
        
        public static Person[] selection_sort_location(Person[] person = null)
        {
            for (int i = 0; i < person.Length; i++)
            {
                for (int j = i + 1; j < person.Length; j++)
                {
                    if (string.Compare(person[j].getLocation, person[i].getLocation) == -1)
                    {
                        swap(i, j, person);
                    }
                }
            }

            return person;
        }

        public static Person[] insertion_sort_location(Person[] person = null)
        {
            Person value;
            int flag;

            for (int i = 0; i < person.Length; i++)
            {
                value = person[i];

                flag = 0;

                for (int j = i - 1; j >= 0 && flag != 1;)
                {
                    if (string.Compare(value.getLocation, person[j].getLocation) == -1)
                    {
                        person[j + 1] = person[j];

                        j--;

                        person[j + 1] = value;
                    }
                    else
                    {
                        flag = 1;
                    }
                }
            }

            return person;
        }
    }

    public class Person
    {
        private string _name;
        private int _age;
        private string _location;

        public Person(string name, int age, string location)
        {
            _name = name;
            _age = age;
            _location = location;
        }

        public string getName
        {
            get
            {
                return _name;
            }

            set
            {
                _name = value;
            }
        }

        public int getAge
        {
            get
            {
                return _age;
            }

            set
            {
                _age = value;
            }
        }

        public string getLocation
        {
            get
            {
                return _location;
            }

            set
            {
                _location = value;
            }
        }
    }
}