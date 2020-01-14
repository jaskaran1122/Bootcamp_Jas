# write function that takes a integer and a list as the input.
# the func should return the index of where the int was found on list

def search(x,list):
	"""
		This function returns the index of where the element x 
		was found on the list
	"""

	length = len(list)
	for num in range(0, length):
		if list[num] == x:
			index = num
			return num


lists = [1, 2, 3, 4, 5, 6, 7, 8]
ans = search(9,lists)
print(ans)


def find_max(list_1):

	"""
	this func returns the max element in list
		param: list - a list of num elements
		returns max val in list
	"""
	max_num = list_1[0]
	for nums in range(0,len(list_1)):
		if max_num <=list_1[nums]:
			max_num = list_1[nums]
	return max_num	

lists_1 = [1,2,464,755,34,8,5,34,7,9,34,4,4,4,5,7,94,2,6,8,2]
ans_2 = find_max(lists_1)
print(ans_2)
