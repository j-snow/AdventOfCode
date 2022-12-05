import Util


def get_set(r):
	s = r.split('-')
	return list(range(int(s[0]), int(s[1])+1))


def find_overlap_count(file_name):
	assignments = Util.split_file_by_new_line(file_name)

	total = 0

	for assignment_pairs in assignments:
		pairs = assignment_pairs.split(',')

		# If strings match one contains the other so add to total and continue, no need to go through the rest
		if pairs[0] == pairs[1]:
			total += 1
			continue

		set1 = get_set(pairs[0])
		set2 = get_set(pairs[1])

		intersection = Util.array_intersect(set1, set2)
		if intersection == set1:
			total += 1
			continue

		if intersection == set2:
			total += 1
			continue

	return total


assert find_overlap_count('4example.txt') == 2
print(find_overlap_count('4input.txt'))