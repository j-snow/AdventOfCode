def get_highest_calories(file_name, no_of_elves):
	with open(file_name) as file:
		lines = file.read().split('\n')

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

print(get_highest_calories('1input.txt', 1))

assert get_highest_calories('1example.txt', 3) == 45000

print(get_highest_calories('1input.txt', 3))
