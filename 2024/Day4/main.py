def parse_input(file):
	array = []
	for line in file:
		array.append(line.strip('\n'))

	return array


def count_xmas(string):
	string = ''.join(string)  # In case it is an array

	count = 0
	count += string.count('XMAS')
	count += string.count('SAMX')
	return count


def get_column(array, i):
	return [row[i] for row in array]


def part_1(array):
	count = 0

	# Horizontal
	horizontal_count = 0
	for row in array:
		horizontal_count += count_xmas(row)
	print('Horizontal count: ' + str(horizontal_count))

	count += horizontal_count

	# Vertical
	vertical_count = 0
	for i in range(0, len(array[0])):
		vertical_count += count_xmas(get_column(array, i))
	print('Vertical count: ' + str(vertical_count))

	count += vertical_count

	# Diagonals
	shifted_left = array.copy()
	row_length = len(shifted_left[0])
	for i in range(0, row_length):
		row = shifted_left[i]
		row = ('-'*(row_length-1)) + row
		row = row[i:]
		row = row + ('-'*i)  # pad the array so we don't get array key errors later
		shifted_left[i] = row

	diagonal_right_count = 0
	for i in range(0, len(shifted_left[0])):
		diagonal_right_count += count_xmas(get_column(shifted_left, i))

	print('Diagonal right count: ' + str(diagonal_right_count))

	count += diagonal_right_count

	shifted_right = array.copy()
	row_length = len(shifted_right[0])
	for i in range(0, row_length):
		row = shifted_right[i]
		row = row + ('-' * (row_length - 1))
		row = row[:((row_length*2)-1-i)]
		row = ('-' * i) + row  # pad the array so we don't get array key errors later
		shifted_right[i] = row

	diagonal_left_count = 0
	for i in range(0, len(shifted_right[0])):
		diagonal_left_count += count_xmas(get_column(shifted_right, i))

	print('Diagonal left count: ' + str(diagonal_left_count))

	count += diagonal_left_count

	print('Final count: ' + str(count))
	return count
