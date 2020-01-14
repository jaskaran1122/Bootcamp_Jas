# import random module
import random

def roll_dice(dice_max):
	"""
	returns a coin flip - random integer between 0 and 1
	if 1 coin lands on heads
	if 0 coin lands on tails
	"""
	return random.randint(0,dice_max)

def monte_carlo(n,dice_max):
	"""
	performs a monte carlo simulation of a coin flip
	[parameter]\t n (int) - number of samples
	[Return]\t None - prints out the results of the simulation
	"""
	num1 = 0
	num2 = 0
	num3 = 0
	num4 = 0
	num5 = 0
	num6 = 0
	exp_count = 0

	while exp_count< n:
		result = roll_dice(dice_max)
		if result == 0:
			num1 += 1
		elif result == 1:
			num2 += 1
		elif result == 2:
			num3 += 1
		elif result == 3:
			num4 += 1
		elif result == 4:
			num5 += 1
		elif result == 5:
			num6 += 1
		exp_count +=1

	print(f"There were {n} simulations performed")

	msg_2 = f"There were {(num1/n)*100}% ones"
	print(msg_2)
	msg = f"There were {(num2/n)*100}% twos"
	print(msg)
	msg_2 = f"There were {(num3/n)*100}% threes"
	print(msg_2)
	msg = f"There were {(num4/n)*100}% fours"
	print(msg)
	msg_2 = f"There were {(num5/n)*100}% fives"
	print(msg_2)
	msg = f"There were {(num6/n)*100}% sixs"
	print(msg)

	for outcome in range(0,dice_max +1):
		count = result.count(outcome)
		msg = f"probability of {outcome} = {(count/n*100)} %"
		print(msg)

monte_carlo(10000,10)
