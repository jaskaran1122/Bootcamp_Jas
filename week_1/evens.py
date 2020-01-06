# the goal of this script is to print out the even number
# between 1 and N (inclusive), where N is a use input.

N = int(input("Enter a upper limit: "))
for number in range(1,N+1):
	if (number%2 == 0):
		print(number)

print("next example with while")
number = 0
while number <N+1:
	if (number%2==0):
		print(number)
	number +=1
	