# Example of a dictionary 
my_personal_info = {
	"name" : "Jaskaran", 
	"DOB" : "01/15/2020",
	"School" : "CCNY",
	"GPA" : 0.5

}
# Dictionaries are known for their "key-value" pair system
#checking if key exists in a dictionary
if "name" in my_personal_info:
	#print("Yes he has a name")
	pass
else:
	#print("Its not in the dictionary")
	pass

# Print all of keys in dictionary
for key in my_personal_info:
	print(key)

#print out all the values in the dictionary (without the key):
for value in my_personal_info.values():
	print(value)