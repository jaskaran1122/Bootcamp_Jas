# TODO: Write a script that prints out the common multiples of 3
#and 5 between the range 0 and N (inclusive). Where is a
#user input

N = int(input("Enter upper limit: "))
counter =0
while counter < N+1:
	if (counter%3 == 0 and counter%5 == 0):
		print(counter)
	counter += 1
