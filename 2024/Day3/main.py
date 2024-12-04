import re
from pprint import pprint


def parse_input_part1(file):
	multiplications = []
	for line in file:
		multiplications.extend(re.findall('mul\((\d{1,3}),(\d{1,3})\)', line))

	return multiplications


def parse_input_part2(file):
	multiplications = []
	for line in file:
		dos = []
		parts = line.split('do()')
		for part in parts:
			dos.append(part.split("don't()")[0])

		for do in dos:
			multiplications.extend(re.findall('mul\((\d{1,3}),(\d{1,3})\)', do))

	return multiplications


def multiply(multiplications):
	total = 0

	for multiplication in multiplications:
		total += int(multiplication[0]) * int(multiplication[1])

	return total