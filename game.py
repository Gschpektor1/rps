import random

class Game:

	def __init__(self):
		pass

	def get_user_item(self):
	# Ask the user to select an item (rock/paper/scissors).
	# Keep asking until the user has selected one of the items – use data validation and looping.
	# Return the item at the end of the function.
		choices = ['Rock', 'Paper', 'Scissors']
		choice = input('Please choose: Rock, Paper, Scissors \n')
		while choice not in choices:
			print('Incorrect input, please select one of the coices')
			choice = input('Please choose: Rock, Paper, Scissors \n')
		return choice

	def get_computer_item(self):
		# Select rock/paper/scissors at random for the computer. Return the item at the end of the function.
		# Use python’s random.choice() function (read about it online).
		return random.choice(['Rock', 'Paper', 'Scissors'])

	def get_game_result(self, user_item, computer_item):
		# Determine the result of the game.
		# Parameters:
		# user_item – the user’s chosen item (rock/paper/scissors)
		# computer_item – the computer’s chosen (random) item (rock/paper/scissors)
		# Return either win, draw, or loss. Where win means that the user has won, draw means the user and
		# the computer got the same item, and loss means that the user has lost.
		if user_item == computer_item:
			print(f'Draw, You both selected {user_item}')
			return 'Draw'
		elif user_item == 'Rock':
			if computer_item == 'Scissors':
				print(f'You Win! Player: Rock, Computer: Scissors')
				return 'Win'
			else:
				print(f'You Lose! Player: Rock, Computer: Paper')
				return 'Loss'
		elif user_item == 'Scissors':
			if computer_item == 'Paper':
				print(f'You Win! Player: Scissors, Computer: Paper')
				return 'Win'
			else:
				print(f'You Lose! Player: Scissors, Computer: Rock')
				return 'Loss'
		elif user_item == 'Paper':
			if computer_item == 'Rock':
				print(f'You Win! Player: Paper, Computer: Rock')
				return 'Win'
			else:
				print(f'You Lose! Player: Paper, Computer: Scissors')
				return 'Loss'



	def play(self):
		# the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
		# Get the user’s item (rock/paper/scissors) and remember it

		# Get a random item for the computer (rock/paper/scissors) and remember it

		# Determine the results of the game by comparing the user’s item and the computer’s item
		# Print the output of the game; something like this: “You selected rock. The computer selected paper.
		# You lose”, “You selected scissors. The computer selected scissors. You drew!”

		# Return the results of the game as a string: win;draw;loss;, where win means that the user has won,
		# draw means the user and the computer got the same item, and loss means that the user has lost.
		user_item = self.get_user_item()
		computer_item = self.get_computer_item()
		result = self.get_game_result(user_item, computer_item)
		return result


