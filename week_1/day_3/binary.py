#finding the roots of a func between a specific region
import math

def f(x):
	return math.sin(x)

def find_root(a,b):
	c=(a+b)/2
	ans = f(c)
	num_iteration = 0
	tolerance = .0000001
	print("outside loop")

	while ans != 0 and num_iteration < 10000 and ans >tolerance:
		num_iteration += 1
		print("value of c: ", c)
		print(num_iteration)
		c=(a+b)/2
		ans = f(c)
		print("ans= ",ans)
		if (f(a)*ans > tolerance):
			print("inif")
			b=c
		elif (ans < tolerance):
			a=c
	if(num_iteration >=1000 and f(c) != 0 and ans > tolerance):
		print("Root cannot be found")
		return None
	else:
		return c



lower = 2
upper = 4
v = find_root(lower,upper)
print(v)