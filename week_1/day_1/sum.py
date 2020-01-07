#the goal of this script is to sum up all of the numbers between 
# N and M (inclusively), where N and M are both user inputs
N = int(input("Enter lower limit: "))
M = int(input("Enter upper limit: "))
sum = 0
for number in range(N,M+1):
	sum += number 
print(sum)

print("using a while loop")
number = 0
sum = 0
print(sum)
while number <= M:
	sum += number
	number +=1
print(sum)
#print("tpyp", type(sum))

