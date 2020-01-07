# TODO: Write a script that prints out the multiples of 3
# between 0 and N where N is the user input

N = int(input("Enter upper limit: "))
counter =0
while counter < N+1:
	if (counter%3 == 0):
		print(counter)
	counter += 1
print("using for loop")
print()

for num in range(0,N+1):
	if (num%3 == 0):
	print(num)
	num += 1
