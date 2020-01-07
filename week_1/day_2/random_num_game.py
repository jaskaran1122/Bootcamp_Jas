# import random
import random

winning_number = random.randint(0,10)

print(winning_number)

num_guess = 5
user_won = False

while num_guess !=0 and user_won == False:
	guess = int(input("Enter your guess! "))
	if guess == winning_number:
		print("Congrats you win! ")
		user_won = True
	else:
		num_guess -= 1
		if user_won == False and num_guess == 0:
			print("Sorry you lose")
			break
		print("Nope, guess again: ")
		
print("Challenge Game")




