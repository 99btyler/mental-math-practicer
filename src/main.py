import random


def get_problem(addition=True, digits_amount=1, easy=True):
	
	places = {}
	for i in range(digits_amount):
		place = [0]*2
		place[0] = random.randint(1, 9)
		if addition:
			place[1] = random.randint(1, 10-place[0]) if easy else random.randint(10-place[0], 9)
		else:
			place[0] = random.randint(1,4) if easy else place[0]
			place[1] = random.randint(1,4) if easy else random.randint(1,9)
		places[i] = place

	numbers = [0]*2
	for key in places:
		numbers[0] = int(str(numbers[0]) + str(places[key][0]))
		numbers[1] = int(str(numbers[1]) + str(places[key][1]))

	problem = []
	if addition:
		problem = [f"{numbers[0]}+{numbers[1]}", numbers[0] + numbers[1]]
	else:
		problem = [f"{numbers[0]}*{numbers[1]}", numbers[0] * numbers[1]]

	return problem

def ask_problem(problem=['1+1', 2]):
	answer = ""
	while not answer.isdigit() or int(answer) != problem[1]:
		answer = input(f"{problem[0]}: ")


min_digits_amount = 2
max_digits_amount = 3

current_addition = True
current_digits_amount = min_digits_amount
current_easy = True

corrects = 0

while True:

	ask_problem(get_problem(addition=current_addition, digits_amount=current_digits_amount, easy=current_easy))
	corrects += 1
	if corrects >= 3:
		current_easy = False

	if input("MOVE ON to next difficulty?(press y)") != "y":
		continue
	else:

		current_easy = True
		corrects = 0

		if current_digits_amount < max_digits_amount:
			current_digits_amount += 1
		else:
			if current_addition:
				current_addition = False
				current_digits_amount = min_digits_amount
			else:
				break

