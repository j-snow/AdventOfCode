def find_low_points(height_map):
	low_points = []
	for y in range(0, len(height_map)):
		for x in range(0, len(height_map[0])):
			point = height_map[y][x]
			surrounding_points = []
			
			if y > 0:
				surrounding_points.append(height_map[y-1][x])

			if y < len(height_map) - 1:
				surrounding_points.append(height_map[y+1][x])

			if x > 0:
				surrounding_points.append(height_map[y][x-1])

			if x < len(height_map[y]) - 1:
				surrounding_points.append(height_map[y][x+1])


			if point < min(surrounding_points):
				low_points.append(point)

	return low_points

test_input = [
'2199943210',
'3987894921',
'9856789892',
'8767896789',
'9899965678'
]

new_test_input = []
for line in test_input:
	new_test_input.append([int(x) for x in list(line)])

test_solution = find_low_points(new_test_input)
assert test_solution == [1,0,5,5]

sum_risk_levels = sum(test_solution) + len(test_solution)
assert sum_risk_levels == 15