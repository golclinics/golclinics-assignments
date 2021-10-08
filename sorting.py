from operator import itemgetter

people = [("Dennis", 44, "Nairobi"), ("Mary", 14, "Kisumu"), ("John", 13, "kwale"), ("Ruth", 24, "Mandera"), ("Karen", 32, "Kakuma"), ("Peter", 29, "Isiolo"), ("Irene", 7, "nyeri"), ("Mohamud", 21, "voi")]

def print_sorted(people):
	people.sort()
	for elem in people:
		print(elem)

print_sorted(people)

#big 0 = 0(n)