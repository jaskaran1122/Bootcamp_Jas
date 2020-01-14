# Practice with lists and functions


# Example:define a function thst returns a list of even numbers
# between A and B (inclusive)

def find_evens(A,B):
	evens = []
	for nums in range(A, B+1):
		if (nums%2 == 0):
			evens.append(nums)

	return evens
print("Printing find_evens")
print(find_evens(2,20))
#Define a func that returns a list of num between 
# A and B (inclusive) that are even multiple of 3

def find_evens_mult_3(A,B):
	evens_mult_3 = []
	for nums in range(A, B+1):
		if (nums%2 == 0 and nums%3 ==0):
			evens_mult_3.append(nums)
	return evens_mult_3
print("Printing find_evens_mult_3")
print(find_evens_mult_3(0,20))