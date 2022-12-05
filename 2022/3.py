import Util


def character_value(char):
	ascii_no = ord(char)
	if char.isupper():
		char_value = ascii_no - 64 + 26
	else:
		char_value = ascii_no - 96

	return char_value


def count_character_values(file_name):
	rucksacks = []
	input = Util.split_file_by_new_line(file_name)
	for rucksack in input:
		no_items = len(rucksack)
		no_in_compartment = int(no_items/2)
		compartments = (rucksack[:no_in_compartment], rucksack[no_in_compartment:])
		rucksacks.append(compartments)

	total = 0
	for rucksack in rucksacks:
		diff = Util.array_intersect(rucksack[0], rucksack[1])
		char = diff[0]
		char_value = character_value(char)

		total += char_value

	return total


def find_badges(file_name):
	input = Util.split_file_by_new_line(file_name)
	total = 0

	while input != []:
		three_rucksacks = input[:3]
		input = input[3:]

		common_character = Util.array_intersect(Util.array_intersect(three_rucksacks[0], three_rucksacks[1]), three_rucksacks[2])
		assert len(common_character) == 1
		char_value = character_value(common_character[0])
		total += char_value

	return total


# Part 1
assert count_character_values('3example.txt') == 157
assert count_character_values('3input.txt') == 7766
print(count_character_values('3input.txt'))

# Part 2
assert find_badges('3example.txt') == 70
assert find_badges('3input.txt') == 2415
print(find_badges('3input.txt'))