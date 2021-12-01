import os

def count_increases(depths):
	count = 0;
	lastdepth = None
	for depth in depths:

		if lastdepth == None:
			lastdepth = depth
			continue

		if depth > lastdepth:
			count = count + 1
		lastdepth = depth

	return count

with open('Day1Input.txt', 'r') as file:
	lines = file.read().split('\n')

	depths = [int(line) for line in lines]

	part1 = count_increases(depths)
	assert part1 == 1832
	print("Day 1, part 1 solution: " + str(part1))

	windows = []
	for i, depth in enumerate(depths):
		if len(depths)-2 == i:
			break

		window = sum(depths[i:i+3])
		windows.append(window)

	part2 = count_increases(windows)
	assert part2 == 1858
	print("Day 1, part 2 solution: " + str(part2))