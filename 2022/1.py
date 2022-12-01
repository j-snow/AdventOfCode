def get_highest_calories(file_name):
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

		return max(elf_calorie_count)


assert get_highest_calories('1example.txt') == 24000

print(get_highest_calories('1input.txt'))
