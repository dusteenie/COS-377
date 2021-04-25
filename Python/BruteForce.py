# Name: Dusty Stepak
# Date: 04.12.2021
# Program: BruteForce.py
# Purpose: Create a brute force password cracking program in Python. 
#          This program asks the user to enter a password, and the 
#          program tries to crack it by checking all possible passwords 
#          with the characters a-zA-Z0-9. Search is limited to passwords 
#          of length 4 or less.



# Prompts the user for a password. Sores value into global variable
# password.
#
# @Author	Dusty Stepak
# @Since	04.12.2021
#
def askForUserInput():
	password = input("Enter password: ")
	print(password) #Debug
	guessPassword(password)



# Loops through every possible value that could be contained within the
# password, up to length 4.
def guessPassword(check):
	guess = "" #Stores the current 'guess'
	passcode = str(check)
	print(passcode)
	# guess = guess[0:i] + letter

	
	# Checks String Length of 1
	# ------------------------------------------------------------------------
	for letter in POSSIBLE_ALPHA_VALUES:
		guess = letter
		print(guess)
		if guess == passcode:
			break

	if guess != passcode:
		for number in POSSIBLE_NUMERIC_VALUES:
			guess = number
			print(guess)
			if guess == passcode:
				break



	# Checks String Length of 2
	# ------------------------------------------------------------------------
	# Letter + Letter
	if guess != passcode:
		for first_letter in POSSIBLE_ALPHA_VALUES:
			for second_letter in POSSIBLE_ALPHA_VALUES:
				guess = str(first_letter + second_letter)
				print(guess)
				if guess == passcode:
					break
			if guess == passcode:
				break
	# Letter + Number
	if guess != passcode:
		for first_letter in POSSIBLE_ALPHA_VALUES:
			for second_number in POSSIBLE_NUMERIC_VALUES:
				guess = str(first_letter + second_number)
				print(guess)
				if guess == passcode:
					break
			if guess == passcode:
				break
	# Number + Number
	if guess != passcode:
		for first_number in POSSIBLE_NUMERIC_VALUES:
			for second_number in POSSIBLE_NUMERIC_VALUES:
				guess = str(first_number + second_number)
				print(guess)
				if guess == passcode:
					break
			if guess == passcode:
				break
	# Number + Letter 
	if guess != passcode:
		for first_number in POSSIBLE_NUMERIC_VALUES:
			for second_letter in POSSIBLE_ALPHA_VALUES:
				guess = str(first_number + second_letter)
				print(guess)
				if guess == passcode:
					break
			if guess == passcode:
				break


	# Checks String Length of 3
	# ------------------------------------------------------------------------
	# Letter + Letter + Letter
	if guess != passcode:
		for first_letter in POSSIBLE_ALPHA_VALUES:
			# Letter + Letter + []
			for second_letter in POSSIBLE_ALPHA_VALUES:
				# Letter, Letter, Letter
				for third_letter in POSSIBLE_ALPHA_VALUES:
					guess = str(first_letter + second_letter + third_letter)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
				# Letter, Letter, Number
				for third_number in POSSIBLE_NUMERIC_VALUES:
					guess = str(first_letter + second_letter + third_number)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
			if guess == passcode:
					break
			# Letter + Number + []
			for second_number in POSSIBLE_NUMERIC_VALUES:
				# Letter, Number, Letter
				for third_letter in POSSIBLE_ALPHA_VALUES:
					guess = str(first_letter + second_number + third_letter)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
				# Letter, Letter, Number
				for third_number in POSSIBLE_NUMERIC_VALUES:
					guess = str(first_letter + second_number + third_number)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
			if guess == passcode:
					break

	if guess != passcode:
		# Number + [] + []
		for first_number in POSSIBLE_NUMERIC_VALUES:
			# Number + Letter + []
			for second_letter in POSSIBLE_ALPHA_VALUES:
				# Letter, Letter, Letter
				for third_letter in POSSIBLE_ALPHA_VALUES:
					guess = str(first_number + second_letter + third_letter)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
				# Number, Letter, Number
				for third_number in POSSIBLE_NUMERIC_VALUES:
					guess = str(first_number + second_letter + third_number)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
			if guess == passcode:
					break
			# Number + Number + []
			for second_number in POSSIBLE_NUMERIC_VALUES:
				# Number, Number, Letter
				for third_letter in POSSIBLE_ALPHA_VALUES:
					guess = str(first_number + second_number + third_letter)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
				# Number, Letter, Number
				for third_number in POSSIBLE_NUMERIC_VALUES:
					guess = str(first_number + second_number + third_number)
					print(guess)
					if guess == passcode:
						break
				if guess == passcode:
					break
			if guess == passcode:
					break

	

	# Checks String Length of 4
	# ------------------------------------------------------------------------
	# Letter + Letter + Letter + Letter
	if guess != passcode:
		# letter + [] + [] + []
		for first_letter in POSSIBLE_ALPHA_VALUES:
			# letter + letter + [] + []
			for second_letter in POSSIBLE_ALPHA_VALUES:
				# letter + letter + letter + []
				for third_letter in POSSIBLE_ALPHA_VALUES:
					# letter + letter + letter + letter
					for fourth_letter in POSSIBLE_ALPHA_VALUES:
						guess = str(first_letter+second_letter+third_letter+fourth_letter)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break
					# letter + letter + letter + number
					for fourth_number in POSSIBLE_NUMERIC_VALUES:
						guess = str(first_letter+second_letter+third_letter+fourth_number)
						print(guess)
						if guess == passcode:
							break


					if guess == passcode:
						break
				if guess == passcode:
					break
				# letter + letter + number + []
				for third_number in POSSIBLE_NUMERIC_VALUES:
					# letter + letter + number + letter
					for fourth_letter in POSSIBLE_ALPHA_VALUES:
						guess = str(first_letter+second_letter+third_number+fourth_letter)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break

					# letter + letter + number + number
					for fourth_number in POSSIBLE_NUMERIC_VALUES:
						guess = str(first_letter+second_letter+third_number+fourth_number)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break

				if guess == passcode:
					break

			if guess == passcode:
				break
			# letter + number + [] + []
			for second_number in POSSIBLE_NUMERIC_VALUES:
				# letter + letter + letter + []
				for third_letter in POSSIBLE_ALPHA_VALUES:
					# letter + letter + letter + letter
					for fourth_letter in POSSIBLE_ALPHA_VALUES:
						guess = str(first_letter+second_number+third_letter+fourth_letter)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break
					# letter + letter + letter + number
					for fourth_number in POSSIBLE_NUMERIC_VALUES:
						guess = str(first_letter+second_number+third_letter+fourth_number)
						print(guess)
						if guess == passcode:
							break	
					if guess == passcode:
						break	

				if guess == passcode:
					break
				# letter + letter + number + []
				for third_number in POSSIBLE_NUMERIC_VALUES:
					# letter + letter + number + letter
					for fourth_letter in POSSIBLE_ALPHA_VALUES:
						guess = str(first_letter+second_number+third_number+fourth_letter)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break

					# letter + letter + number + number
					for fourth_number in POSSIBLE_NUMERIC_VALUES:
						guess = str(first_letter+second_number+third_number+fourth_number)
						print(guess)
						if guess == passcode:
							break
					if guess == passcode:
						break


				if guess == passcode:
					break
			if guess == passcode:
					break


		if guess != passcode:
			# number + [] + [] + []
			for first_number in POSSIBLE_ALPHA_VALUES:
				# number + letter + [] + []
				for second_letter in POSSIBLE_ALPHA_VALUES:
					# number + letter + letter + []
					for third_letter in POSSIBLE_ALPHA_VALUES:
						# number + letter + letter + letter
						for fourth_letter in POSSIBLE_ALPHA_VALUES:
							guess = str(first_number+second_letter+third_letter+fourth_letter)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break	

						# number + letter + letter + number
						for fourth_number in POSSIBLE_NUMERIC_VALUES:
							guess = str(first_number+second_letter+third_letter+fourth_number)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break

					if guess == passcode:
						break
					# number + letter + number + []
					for third_number in POSSIBLE_NUMERIC_VALUES:
						# number + letter + number + letter
						for fourth_letter in POSSIBLE_ALPHA_VALUES:
							guess = str(first_number+second_letter+third_number+fourth_letter)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
						# number + letter + number + number
						for fourth_number in POSSIBLE_NUMERIC_VALUES:
							guess = str(first_number+second_letter+third_number+fourth_number)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
					if guess == passcode:
						break
				if guess == passcode:
					break
				# number + number + [] + []
				for second_number in POSSIBLE_NUMERIC_VALUES:
					# number + letter + letter + []
					for third_letter in POSSIBLE_ALPHA_VALUES:
						# number + letter + letter + letter
						for fourth_letter in POSSIBLE_ALPHA_VALUES:
							guess = str(first_number+second_number+third_letter+fourth_letter)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
						# number + letter + letter + number
						for fourth_number in POSSIBLE_NUMERIC_VALUES:
							guess = str(first_number+second_number+third_letter+fourth_number)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
					if guess == passcode:
						break
					# number + letter + number + []
					for third_number in POSSIBLE_ALPHA_VALUES:
						# number + letter + number + letter
						for fourth_letter in POSSIBLE_ALPHA_VALUES:
							guess = str(first_number+second_number+third_number+fourth_letter)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
						# number + letter + number + number
						for fourth_number in POSSIBLE_NUMERIC_VALUES:
							guess = str(first_number+second_number+third_number+fourth_number)
							print(guess)
							if guess == passcode:
								break
						if guess == passcode:
							break
					if guess == passcode:
						break
				if guess == passcode:
					break

	print()
	print("You've been HACKED!")
	print("Your password: " + str(passcode))
	print("Our password: " + str(guess))


# --------------------------------------------------------------------------
# Global Variable Declaration
# --------------------------------------------------------------------------
# Constants
POSSIBLE_ALPHA_VALUES = ["A","a","B","b","C","c","D","d","E","e","F","f","G","g","H","h","I","i","J","j","K","k","L","l","M","m","N","n","O","o","P","p","Q","q","R","r","S","s","T","t","U","u","V","v","W","w","X","x","Y","y","Z","z"]
POSSIBLE_NUMERIC_VALUES = ["0","1","2","3","4","5","6","7","8","9"]


# --------------------------------------------------------------------------
# Main function call
# --------------------------------------------------------------------------
askForUserInput()
