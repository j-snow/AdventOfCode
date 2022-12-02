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


losing_combinations = {
	'B': 'X',
	'C': 'Y',
	'A': 'Z',
}

winning_combinations_against = {
	'C': 'X',
	'A': 'Y',
	'B': 'Z',
}


# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
def rock_paper_scissors_choice(file_name):
	rounds = Util.split_file_by_new_line(file_name)

	my_score_total = 0

	for round in rounds:
		my_score = 0

		split = round.split(' ')
		their_choice = split[0]
		wld = split[1]

		if wld == 'X':
			# Lose
			my_choice = losing_combinations[their_choice]
		elif wld == 'Y':
			# Draw
			my_choice = their_choice
			my_score += 3
		elif wld == 'Z':
			my_choice = winning_combinations_against[their_choice]
			my_score += 6

		my_score += scoring[my_choice]
		my_score_total += my_score

	return my_score_total


assert rock_paper_scissors_choice('2example.txt') == 12

p2 = rock_paper_scissors_choice('2input.txt')
print(p2)
assert p2 == 13889
