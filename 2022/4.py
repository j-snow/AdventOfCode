import Util


def get_set(r):
	s = r.split('-')
	return list(range(int(s[0]), int(s[1])+1))


def find_overlap_count(file_name):
	assignments = Util.split_file_by_new_line(file_name)

	total = 0

	for assignment_pairs in assignments:
		pairs = assignment_pairs.split(',')

		first = pairs[0].split('-')
		first = (int(first[0]), int(first[1]))
		second = pairs[1].split('-')
		second = (int(second[0]), int(second[1]))

		if first[0] <= second[0] and first[1] >= second[1]:
			print([first, second])
			total += 1
			continue

		if second[0] <= first[0] and second[1] >= first[1]:
			print([first, second])
			total += 1
			continue

	return total


assert find_overlap_count('4example.txt') == 2
assert find_overlap_count('4input.txt') == 560
print(find_overlap_count('4input.txt'))