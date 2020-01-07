num = int(input("Enter a number: "))
min_num = 3
max_num = 15
if num > min_num and num < max_num:
	print("Nice")
elif num > min_num - 2 and num < max_num + 2:
	print("kind of nice")
else:
	print("Not nice")