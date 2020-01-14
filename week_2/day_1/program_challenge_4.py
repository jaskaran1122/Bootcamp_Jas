# Programing challenge 4 
# finding the difference between 2 lists without use of sets

def find_diffs(a,b):
	differences = []
	for element in a:
		if element not in b:
			differences.append(element)

	for element in b:
		if element not in a:
			differences.append(element)

	return differences

test_1 = [1,2,3]
test_2 = [1,2,3]

print(find_diffs(test_1,test_2))
