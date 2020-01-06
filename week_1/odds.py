# the goal of the script is to print all the odd numbers between 0 and 
#N inclusively where N is the user input

N = int(input("Enter a upper limit: "))
for number in range(1,N+1):
	if (number%2 == 1):
		print(number)

print("next example with while")
number = 0
while number <N+1:
	if (number%2==1):
		print(number)
	number +=1
