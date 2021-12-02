with open('Day2Input.txt') as file:
	commands = file.readlines()

	horizontal_pos = 0
	depth = 0
	aim = 0

	for command in commands:
		split = command.split(' ')
		direction = split[0]
		amount = int(split[1])

		match direction:
			case 'forward':
				horizontal_pos = horizontal_pos + amount
				depth  = depth + (aim * amount)
			case 'up':
				aim = aim - amount
			case 'down':
				aim = aim + amount
			case _:
				raise ValueError('direction ' + direction + ' not recognised')

	solution1 = horizontal_pos*aim # aim is the old depth from part one
	assert solution1 == 1714680
	print("Day 2 part 1 solution: " + str(solution1))

	solution2 = horizontal_pos*depth
	assert solution2 == 1963088820
	print("Day 2 part 2 solution: " + str(solution2))