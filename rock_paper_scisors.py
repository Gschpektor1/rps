from game import Game
game = Game()

def get_user_menu_choice():
	# this should display a simple menu, get the user’s choice (with data validation), and return the choice.
	# No looping should occur here.
	# The possibles choices are : Play a new game or Show scores or Quit
	choices = ['Play a new game', 'Show scores', 'Quit']
	choice = input('Please select one of: \n (P)lay a new game, (S)how scores, (Q)uit \n')
	while choice not in ['P', 'S', 'Q']:
		print('Incorrect input, please select one of the coices')
		choice = input('Please select one of by using the number: \n Play a new game, Show scores, Quit \n')
	return choice

def print_results(results):
	# this should print the results of the games played. It should have a single parameter named results;
	# which will be a dictionary of the results of the games played. It should display these results in a user-friendly way,
	# and thank the user for playing.
	message = '\n Thank you for playing'
	print(results)

def main():
	# the main function. It should take care of 3 things:
	# Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide.
	# (Make use of the get_user_menu_choice function)

	# When the user chooses to play a game:
	# Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
	# Remember the results of every game that is played.

	# When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
	results = {
	'Win' : 0,
	'Loss': 0,
	'Draw': 0
	}

	playing = True
	while True:
		choice = get_user_menu_choice()
		if choice == 'P':
			result = game.play()
			results[result] += 1
		elif choice == 'S':
			print_results(results)
		else:
			print_results(results)
			break

main()

