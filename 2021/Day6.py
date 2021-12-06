def prepare_array(array):
	prepared_array = []
	for x in range(0,9):
		prepared_array.append(0)

	for num in array:
		prepared_array[num] = prepared_array[num] + 1

	return prepared_array

def add_fish(fish, amount):
	if amount == 0:
		return fish
	else:
		new = fish.pop(0)
		fish[6] = fish[6] + new
		fish.append(new)
		
		return add_fish(fish, amount-1)


# Examples
test_input = [3,4,3,1,2]

prepared_test_input = prepare_array(test_input)
test_result = add_fish(prepared_test_input, 18)
assert sum(test_result) == 26
assert test_result == prepare_array([6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8])

prepared_test_input = prepare_array(test_input)
test_result = add_fish(prepared_test_input, 80)
assert sum(test_result) == 5934

prepared_test_input = prepare_array(test_input)
test_result = add_fish(prepared_test_input, 256)
assert sum(test_result) == 26984457539


# Solutions
input = [1,1,1,1,1,5,1,1,1,5,1,1,3,1,5,1,4,1,5,1,2,5,1,1,1,1,3,1,4,5,1,1,2,1,1,1,2,4,3,2,1,1,2,1,5,4,4,1,4,1,1,1,4,1,3,1,1,1,2,1,1,1,1,1,1,1,5,4,4,2,4,5,2,1,5,3,1,3,3,1,1,5,4,1,1,3,5,1,1,1,4,4,2,4,1,1,4,1,1,2,1,1,1,2,1,5,2,5,1,1,1,4,1,2,1,1,1,2,2,1,3,1,4,4,1,1,3,1,4,1,1,1,2,5,5,1,4,1,4,4,1,4,1,2,4,1,1,4,1,3,4,4,1,1,5,3,1,1,5,1,3,4,2,1,3,1,3,1,1,1,1,1,1,1,1,1,4,5,1,1,1,1,3,1,1,5,1,1,4,1,1,3,1,1,5,2,1,4,4,1,4,1,2,1,1,1,1,2,1,4,1,1,2,5,1,4,4,1,1,1,4,1,1,1,5,3,1,4,1,4,1,1,3,5,3,5,5,5,1,5,1,1,1,1,1,1,1,1,2,3,3,3,3,4,2,1,1,4,5,3,1,1,5,5,1,1,2,1,4,1,3,5,1,1,1,5,2,2,1,4,2,1,1,4,1,3,1,1,1,3,1,5,1,5,1,1,4,1,2,1]

solution = sum(add_fish(prepare_array(input), 80))
assert solution == 374994
print("Day 6, part 1: " + str(solution))

solution = sum(add_fish(prepare_array(input), 256))
assert solution == 1686252324092
print("Day 6, part 2: " + str(solution))