import os

with open('Day1Input.txt', 'r') as file:
	lines = file.read().split('\n')

	count = 0;
	lastdepth = None
	for line in lines:
		depth = int(line)

		if lastdepth == None:
			lastdepth = depth
			continue

		if depth > lastdepth:
			count = count + 1
		lastdepth = depth

	print("Day 1 solution: " + str(count))