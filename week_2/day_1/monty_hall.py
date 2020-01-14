import random 

def organize_game():
	door_contents = [1,0,0]
	random.shuffle(door_contents)

	for i in range(0,len(door_contents)):
		if door_contents[i] == 1:
			winning_door = i

	return door_contents, winning_door

def game_time():
	door_nums = [0,1,2]

	door_contents, winning_choice = organize_game()

	# We need the consestant to make a choice
	door_chosen = random.coice(door_nums)

	# Now we need the game show host to open another door
	# The game show hpst must open a door that does not have
	# but the door must also not be the one that the contestant picked
	unavailable_doors = [door_chosen, winning_door]
	door_to_open = set(door_nums).difference(unavailable_doors)
	door_to_open = door_to_open.pop()

	#see if the contestant won or lost
	switched_win = False
	stayed_win = False



	pass

# list_1= [1,1,1,1,1,1,5,6,7]
# my_set = set(list_1)
# print(my_set)
# list_2 = [1,6,7]
# list_3 = []
# list_3 = set(list_1).difference(list_2)

# print(list_3)


#help(random.shuffle)