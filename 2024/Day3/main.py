import re


def parse_input(file):
	multiplications = []
	for line in file:
		multiplications.extend(re.findall('mul\((\d{1,3}),(\d{1,3})\)', line))

	return multiplications

def is_safe(report):
	safe = True
	contains_positive = False
	contains_negative = False
	diffs = [report[i] - report[i + 1] for i in range(0, len(report) - 1)]
	for number in diffs:
		if number == 0:
			safe = False
			continue
		if abs(number) > 3:
			safe = False
			continue
		if number < 0:
			contains_negative = True
		if number > 0:
			contains_positive = True
		if contains_positive and contains_negative:
			safe = False
			continue

	return safe

def part_1(multiplications):
	total = 0

	for multiplication in multiplications:
		total += int(multiplication[0]) * int(multiplication[1])

	return total

def part_2(reports):
	total = 0

	for multiplication in multiplications:
		total += int(multiplication[0]) * int(multiplication[1])

	return total
