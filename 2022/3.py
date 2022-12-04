import Util


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
		diff = list(set(rucksack[0]) & set(rucksack[1]))
		char = diff[0]
		char_no = None
		ascii_no = ord(char)
		if char.isupper():
			char_no = ascii_no - 64 + 26
		else:
			char_no = ascii_no - 96

		total += char_no

	return total


assert count_character_values('3example.txt') == 157
assert count_character_values('3input.txt') == 7766
print(count_character_values('3input.txt'))
