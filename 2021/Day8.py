def normalise_input(array):
	normalised_input = array

	normalised_input = [line.strip().split('|') for line in normalised_input]
	normalised_input = [([line[0].strip().split(' '), line[1].strip().split(' ')]) for line in normalised_input]

	return normalised_input

with open('Day8Input.txt') as file:
	input = normalise_input(file.readlines())

	count = 0
	for line in input:
		for output in line[1]:
			if len(output) in [2,3,4,7]:
				count = count + 1

	assert count == 493
	print("Day 8, part 1: " + str(count))