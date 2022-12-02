def split_file_by_new_line(file_name):
	with open(file_name) as file:
		lines = file.read().split('\n')

		return lines
