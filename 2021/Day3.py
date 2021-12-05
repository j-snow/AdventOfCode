with open('Day3Input.txt') as file:
	diagnostic_report = file.readlines()
	split = []
	for line in diagnostic_report:
		array = list(line)
		if array[-1:][0] == '\n':
			array = array[:-1]

		array = [int(x) for x in array]
		split.append(array)

	count = []
	for x in range(0, len(split[0])):
		count.append(0)
		for line in split:
			count[x] = count[x] + line[x]


	gamma = [str(int(x > len(diagnostic_report)/2)) for x in count]
	gamma_binary = ''.join(gamma)
	gamma_decimal = int(gamma_binary, 2)

	epsilon = [str(int(int(x) < 1)) for x in gamma]
	epsilon_binary = ''.join(epsilon)
	epsilon_decimal = int(epsilon_binary, 2)

	part_1_solution = gamma_decimal * epsilon_decimal
	assert part_1_solution == 738234
	print('Day 3, part 1: ' + str(part_1_solution))