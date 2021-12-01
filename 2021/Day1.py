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

	print("Day 1 solution: " + str(count_increases(depths)))

	windows = []
	for i, depth in enumerate(depths):
		if len(depths)-2 == i:
			break

		window = sum(depths[i:i+3])
		windows.append(window)

	print("Day 2 solution: " + str(count_increases(windows)))