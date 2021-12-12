import math

def find_low_points(height_map):
	basins = []
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
				basins.append({
					'Low': point,
					'X': x,
					'Y': y,
					'Size': find_basin_size(height_map, x, y)
				})

	return basins

def find_basin_size(height_map, x, y):
	points_checked = []
	points_to_check = [(x,y)]

	while len(points_to_check) > 0:
		new_points_to_check = points_to_check.copy()
		for x, y in points_to_check:
			new_points_to_check.remove((x,y))

			if height_map[y][x] != 9:
				points_checked.append((x,y))
				neighbors = [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]

				for neighbor in neighbors:
					if neighbor in points_checked:
						continue
					if neighbor in new_points_to_check:
						continue
					if neighbor[0] < 0:
						continue
					if neighbor[1] < 0:
						continue
					if neighbor[0] > len(height_map[0]) - 1:
						continue
					if neighbor[1] > len(height_map) - 1:
						continue

					new_points_to_check.append(neighbor)


		points_to_check = new_points_to_check

	return len(points_checked)

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
test_low_points = [basin['Low'] for basin in test_solution]
assert test_low_points == [1,0,5,5]

sum_risk_levels = sum(test_low_points) + len(test_low_points)
assert sum_risk_levels == 15

test_basins = [basin['Size'] for basin in test_solution]
test_basins.sort()
assert math.prod(test_basins[-3:]) == 1134

with open('Day9Input.txt') as file:
	input = []
	for line in file:
		input.append([int(x) for x in list(line.strip())])

	solution_basins = find_low_points(input)
	solution_low_points = [basin['Low'] for basin in solution_basins]

	solution = sum(solution_low_points) + len(solution_low_points)
	assert solution == 494
	print("Day 9, solution 1: " + str(solution))

	solution_basins_sizes = [basin['Size'] for basin in solution_basins]
	solution_basins_sizes.sort()
	solution_2 = math.prod(solution_basins_sizes[-3:])
	assert solution_2 == 1048128
	print("Day 9, solution 2: " + str(solution_2))
