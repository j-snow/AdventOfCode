import unittest
import main

class D4TestCase(unittest.TestCase):
	def test_part_1_example(self):
		with open('./Example') as file:
			input = main.parse_input(file)
			self.assertEqual(18, main.part_1(input))

	def test_part_1_input(self):
		with open('./Input') as file:
			input = main.parse_input(file)
			result = main.part_1(input)
			print("Day 4 part 1 : " + str(result))
			self.assertEqual(2493, result)

	def test_part_2_example(self):
		with open('./Example') as file:
			input = main.part_2(file)
			self.assertEqual(None, main.multiply(input))

	def test_part_2_input(self):
		with open('./Input') as file:
			input = main.parse_input(file)
			result = main.part_2(input)
			print("Day 4 part 2 : " + str(result))
			self.assertEqual(None, result)


if __name__ == '__main__':
	unittest.main()
