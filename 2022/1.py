import Util


def get_highest_calories(file_name, no_of_elves):
	lines = Util.split_file_by_new_line(file_name)

	elves = []
	elf = []
	for line in lines:
		if line == '':
			elves.append(elf)
			elf = []
		else:
			line = int(line)
			elf.append(line)
	elves.append(elf)

	elf_calorie_count = [sum(x) for x in elves]
	elf_calorie_count.sort(reverse=True)

	top_elves = elf_calorie_count[:no_of_elves]
	return sum(top_elves)


assert get_highest_calories('1example.txt', 1) == 24000

p1 = get_highest_calories('1input.txt', 1)
assert p1 == 71124
print(p1)

assert get_highest_calories('1example.txt', 3) == 45000

p2 = get_highest_calories('1input.txt', 3)
assert p2 == 204639
print(p2)
