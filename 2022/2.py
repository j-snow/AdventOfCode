import Util

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
scoring = {
	'A': 1,
	'B': 2,
	'C': 3,
	'X': 1,
	'Y': 2,
	'Z': 3,
}

winning_combinations = {
	'X': 'C',
	'Y': 'A',
	'Z': 'B',
}

def rock_paper_scissors_score(file_name):
	rounds = Util.split_file_by_new_line(file_name)

	my_score_total = 0

	for round in rounds:
		my_score = 0
		their_score = 0

		split = round.split(' ')
		their_choice = split[0]
		my_choice = split[1]

		my_choice_score = scoring[my_choice]
		their_choice_score = scoring[their_choice]

		my_score = my_score + my_choice_score
		their_score = their_score + their_choice_score

		if my_choice_score == their_choice_score:
			# Draw
			my_score = my_score + 3
		elif winning_combinations[my_choice] == their_choice:
			my_score = my_score + 6

		my_score_total = my_score_total + my_score

	return my_score_total

assert rock_paper_scissors_score('2example.txt') == 15

p1 = rock_paper_scissors_score('2input.txt')
print(p1)
assert p1 == 14827
