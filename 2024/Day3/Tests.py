import unittest
import main

class D3TestCase(unittest.TestCase):
	def test_part_1_example(self):
		with open('2024/Day3/Example') as file:
			input = main.parse_input(file)
			self.assertEqual(161, main.part_1(input))

	def test_part_1_input(self):
		with open('2024/Day3/Input') as file:
			input = main.parse_input(file)
			result = main.part_1(input)
			self.assertEqual(178538786, result)
			print("Day 3 part 1 : " + str(result))

	def test_part_2_example(self):
		with open('2024/Day3/Example') as file:
			input = main.parse_input(file)
			self.assertEqual(None, main.part_2(input))

	def test_part_2_input(self):
		with open('2024/Day3/Input') as file:
			input = main.parse_input(file)
			result = main.part_2(input)
			self.assertEqual(None, result)
			print("Day 3 part 2 : " + str(result))


if __name__ == '__main__':
	unittest.main()
