import unittest
import main

class D3TestCase(unittest.TestCase):
	def test_part_1_example(self):
		with open('2024/Day3/Example') as file:
			input = main.parse_input_part1(file)
			self.assertEqual(161, main.multiply(input))

	def test_part_1_input(self):
		with open('2024/Day3/Input') as file:
			input = main.parse_input_part1(file)
			result = main.multiply(input)
			self.assertEqual(178538786, result)
			print("Day 3 part 1 : " + str(result))

	def test_part_2_example(self):
		with open('2024/Day3/P2Example') as file:
			input = main.parse_input_part2(file)
			self.assertEqual(48, main.multiply(input))

	def test_part_2_input(self):
		with open('2024/Day3/Input') as file:
			input = main.parse_input_part2(file)
			result = main.multiply(input)
			print("Day 3 part 2 : " + str(result))
			self.assertEqual(102467299, result)


if __name__ == '__main__':
	unittest.main()
