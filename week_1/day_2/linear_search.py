# write function that takes a integer and a list as the input.
# the func should return the index of where the int was found on list

def search(x,list):
	length = len(list)
	for num in range(0, length):
		if list[num] == x:
			index = num
			return num
		else:


list = [1,2,3,4,5,6,7,8]
search(5,list)