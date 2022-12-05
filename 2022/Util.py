def split_file_by_new_line(file_name):
	with open(file_name) as file:
		lines = file.read().split('\n')

		return lines


def array_intersect(arr1, arr2):
	intersected_set = set(arr1) & set(arr2)
	return list(intersected_set)
