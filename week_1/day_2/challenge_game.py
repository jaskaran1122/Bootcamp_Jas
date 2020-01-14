# Challenge Game
print("Challenge Game")

import random

winning_number = random.randint(0,100)

print("Winning Number: ", winning_number)

num_guess = 5
user_won = False
guess_attempt = 0
user_guess = []

while num_guess !=0 and user_won == False:
	print("Your previous guesses: ", user_guess)
	print("Attempts so far: ", guess_attempt+1)
	guess = int(input("Enter your guess!: "))
	user_guess.append(guess)
	if guess == winning_number:
		print("Congrats you win! ")
		user_won = True
	else:
		num_guess -= 1
		if user_won == False and num_guess == 0:
			print("Sorry you lose")
			break
		else:
			if winning_number-10 < guess < winning_number+10:
				if winning_number-5 < guess < winning_number+5:
					print("Hotter")
				else:
					print("Warmer")
			else:
		 		print("Your cold as ice!")

		print("Guess again: ")
	guess_attempt += 1
		




