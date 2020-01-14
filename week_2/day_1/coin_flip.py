# import random module
import random

def flip_coin():
	"""
	returns a coin flip - random integer between 0 and 1
	if 1 coin lands on heads
	if 0 coin lands on tails
	"""
	return random.randint(0,1)

def monte_carlo(n):
	"""
	performs a monte carlo simulation of a coin flip
	[parameter]\t n (int) - number of samples
	[Return]\t None - prints out the results of the simulation
	"""
	head_count = 0
	tail_count = 0
	exp_count = 0

	while exp_count< n:
		result = flip_coin()
		if result == 1:
			head_count += 1
		elif result == 0:
			tail_count += 1
		exp_count +=1

	print(f"There were {n} simulations performed")
	msg = f"There were {(head_count/n)*100}% heads"
	print(msg)
	msg_2 = f"There were {(tail_count/n)*100}% tails"
	print(msg_2)

monte_carlo(100)


