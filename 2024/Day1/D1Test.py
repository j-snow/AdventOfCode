import unittest
import D1


class D1TestCase(unittest.TestCase):
	def test_add_up_location_distances(self):
		with open('2024/Day1/D1TestInput.txt') as file:
			pairs = D1.parse_input(file)
			self.assertEqual(11, D1.add_up_location_distances(pairs))

	def test_add_up_location_distances_final(self):
		with open('2024/Day1/D1Input.txt') as file:
			pairs = D1.parse_input(file)
			self.assertEqual(2176849, D1.add_up_location_distances(pairs))

	def test_similarity_score(self):
		with open('2024/Day1/D1TestInput.txt') as file:
			pairs = D1.parse_input(file)
			self.assertEqual(31, D1.similarity_score(pairs))

	def test_similarity_score_final(self):
		with open('2024/Day1/D1Input.txt') as file:
			pairs = D1.parse_input(file)
			self.assertEqual(23384288, D1.similarity_score(pairs))


if __name__ == '__main__':
	unittest.main()
