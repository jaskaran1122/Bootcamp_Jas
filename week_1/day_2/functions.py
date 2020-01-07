#define f(x) = x + 1
def f(x):
	ans = x+1
	return ans

my_solution = f(1)

print(my_solution)

# try for yourself:
# define a function 

def g(x):
	ans_2 = x**4 + x**2 + 1
	return ans_2

my_solution_2 = g(1), g(2), g(3)
print(my_solution_2)

#functions with multiple returns
def get_first_two_evens():
	return 2,4

even_1,even_2 = get_first_two_evens()
print(even_1)
print(even_2)

#function with no returns (void in c++)
def print_even(N):
	for num in range(1,N+1):
		if (num%2 == 0):
			print(num)

#print(print_even(10))

print("Common mult of 3 and 7")

# Write a func that takes N as in an input and print
# all common multiples of 3 and 7, between 0 and N (inclusive)

def comomon_mult_3_7(N):
	#N = int(input("Enter upper limit: "))
	counter =0
	while counter < N+1:
		if (counter%3 == 0 and counter%7 == 0):
			print(counter)
		counter += 1
comomon_mult_3_7(100)
print("Common mult of x and y")

#define a function that takes 3 inputs :x,y,N
#the function will find all the common multiples of x any y
# between 0 and N

print("Common mult of x and y")



def comomon_mult_x_y(x,y,N):
	counter =0
	while counter < N+1:
		if (counter%x == 0 and counter%y == 0):
			print(counter)
		counter += 1
comomon_mult_x_y(3,7,100)






















