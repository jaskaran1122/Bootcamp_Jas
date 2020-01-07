my_first_list = [2,4,6,8]
print("Printing index 0 and 1")
print(my_first_list[0])
print(my_first_list[2])

print("Print len of list")
length = len(my_first_list)
print(length)

print("Print all number with loop")
for index in range(0, length):
	print(my_first_list[index])

print("Printing the list")
print(my_first_list)
print("Adding and printing new index")
my_first_list.append(10)
print(my_first_list)

#make a list of even numbers up to 12 (inclusive)
print("List of even numbers up to 12 (inclusive)")

even_list = []
for num in range(1,13):
	if (num%2 == 0):
		even_list.append(num)
print(even_list)

length_1 = len(even_list)

#even_list.clear()
#print("Even_list after .clear method")
#print(even_list)

print("Pop method")
for i in range(0, length_1-1):
	if even_list[i] == 10:
		ten = even_list.pop(i)
		index_val_of_ten = i

print("List after popping an element")
print(even_list)
print("The value of ten", ten)

even_list.insert(index_val_of_ten, ten)
print("Using insert, to put the 10 back")

print(sorted(even_list))























