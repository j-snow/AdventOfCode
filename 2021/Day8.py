def normalise_input(array):
	normalised_input = array

	normalised_input = [line.strip().split('|') for line in normalised_input]
	normalised_input = [([line[0].strip().split(' '), line[1].strip().split(' ')]) for line in normalised_input]

	return normalised_input

def display_number(number, mapping):
	segments = []
	for letter in number:
		segments.append(mapping.index(letter))

	segments.sort()
	valid_combinations = [
		[0, 1, 2, 3, 4, 5], # 0
		[1, 2], # 1
		[0, 1, 3, 4, 6] , # 2
		[0, 1, 2, 3, 6], # 3
		[1, 2, 5, 6], # 4
		[0,2,3,5,6], # 5
		[0, 2, 3, 4, 5, 6], # 6
		[0,1, 2], # 7
		[0, 1, 2, 3, 4, 5, 6], # 8
		[0, 1, 2, 3, 5, 6], # 9
	]

	return valid_combinations.index(segments)

def display_numbers(numbers, mapping):
	display = []
	for number in numbers:
		display.append(str(display_number(number, mapping)))

	display = ''.join(display)

	return int(display)

def find_mapping(input):
	numbers = input
	numbers = numbers[0]
	mapping = ['','','','','','','']

	# Find segment 0
	numbers_dict = {}
	for number in numbers:
		length = len(number)
		if length == 2:
			numbers_dict[1] = number
		elif length == 3:
			numbers_dict[7] = number
		elif length == 4:
			numbers_dict[4] = number
		elif length == 7:
			numbers_dict[8] = number

	for letter in numbers_dict[7]:
		if letter not in numbers_dict[1]:
			mapping[0] = letter

	# Find segment 1 and 2
	no_full_right = [];
	for number in numbers:
		# get rid of any numbers that share segments with 1
		# leaving just 2,5,6 wich each contain half of 1
		if not (numbers_dict[1][0] in number and numbers_dict[1][1] in number):
			no_full_right.append(number)

	first = 0
	second = 0
	for number in no_full_right:
		if len(number) == 6:
			numbers_dict[6] = number
		if numbers_dict[1][0] in number:
			first = first + 1
		if numbers_dict[1][1] in number:
			second = second + 1

	if first < second:
		mapping[1] = numbers_dict[1][0]
		mapping[2] = numbers_dict[1][1]
	else:
		mapping[1] = numbers_dict[1][1]
		mapping[2] = numbers_dict[1][0]

	for number in no_full_right:
		if mapping[1] in number:
			numbers_dict[2] = number
		elif mapping[2] in number and len(number) == 5:
			numbers_dict[5] = number

	# Find segment 4
	for letter in numbers_dict[6]:
		if letter not in numbers_dict[5]:
			mapping[4] = letter

	# Find segment 5
	for letter in numbers_dict[5]:
		if letter not in numbers_dict[2] and letter not in mapping:
			mapping[5] = letter

	# Find segment 6
	for letter in numbers_dict[4]:
		if letter not in mapping:
			mapping[6] = letter

	# Find segment 3
	for letter in numbers_dict[8]:
		if letter not in mapping:
			mapping[3] = letter

	return mapping

test_input = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
test_input = normalise_input(test_input)
mapping = find_mapping(test_input[0])
assert mapping == ['d','a','b','c','g','e','f']
assert display_number('acedgfb', mapping) == 8
assert display_number('cdfbe', mapping) == 5
assert display_number('gcdfa', mapping) == 2
assert display_number('fbcad', mapping) == 3
assert display_number('dab', mapping) == 7
assert display_number('cefabd', mapping) == 9
assert display_number('cdfgeb', mapping) == 6
assert display_number('eafb', mapping) == 4
assert display_number('cagedb', mapping) == 0
assert display_number('ab', mapping) == 1

assert display_numbers(test_input[0][1], mapping) == 5353


with open('Day8Input.txt') as file:
	input = normalise_input(file.readlines())

	count = 0
	for line in input:
		for output in line[1]:
			if len(output) in [2,3,4,7]:
				count = count + 1

	assert count == 493
	print("Day 8, part 1: " + str(count))

	total = 0
	for line in input:
		mapping = find_mapping(line)
		value = display_numbers(line[1], mapping)
		total = total +value

	assert total == 1010460
	print("Day 8, part 2: " + str(total))