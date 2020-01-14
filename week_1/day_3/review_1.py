# Make a function that takes 2 inputs:
# an lower limit and upper limit. Func should return
# all mult of 5  between lower and upper bounds

def find_mults(N,M):
	mults = []
#	N = int(inputs("Enter lower limit: "))
#	M = int(inputs("Enter upper limit: "))
	for nums in range(N,M+1):
		if (nums%5 == 0):
			mults.append(nums)

	return mults

print(find_mults(1,100))
