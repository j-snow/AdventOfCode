import unittest
import D2

class D2TestCase(unittest.TestCase):
	def test_part_1_example(self):
		with open('2024/Day2/D2Example') as file:
			input = D2.parse_input(file)
			self.assertEqual(2, D2.part_1(input))

	def test_part_1_input(self):
		with open('2024/Day2/D2Input') as file:
			input = D2.parse_input(file)
			result = D2.part_1(input)
			self.assertEqual(472, result)
			print("Day 2 part 1 : " + str(result))

	def test_part_2_example(self):
		with open('2024/Day2/D2Example') as file:
			input = D2.parse_input(file)
			self.assertEqual(4, D2.part_2(input))

	def test_part_2_input(self):
		with open('2024/Day2/D2Input') as file:
			input = D2.parse_input(file)
			result = D2.part_2(input)
			self.assertEqual(520, result)
			print("Day 2 part 2 : " + str(result))


if __name__ == '__main__':
	unittest.main()
