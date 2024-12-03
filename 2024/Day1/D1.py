import re


def parse_input(file):
	locations1 = []
	locations2 = []
	for line in file:
		results = re.search("(\d+)\s+(\d+)", line)
		locations1.append(int(results.group(1)))
		locations2.append(int(results.group(2)))

	locations1.sort()
	locations2.sort()

	pairs = list(zip(locations1, locations2))

	return pairs


def add_up_location_distances(pairs):
	total = 0
	for pair in pairs:
		total += abs(pair[1] - pair[0])

	return total


def similarity_score(pairs):
	total = 0
	rhs = [pair[1] for pair in pairs]
	for pair in pairs:
		total += pair[0] * rhs.count(pair[0])

	return total


with open('2024/Day1/D1Input.txt') as file:
	pairs = parse_input(file)
	print(add_up_location_distances(pairs))
	print(similarity_score(pairs))
