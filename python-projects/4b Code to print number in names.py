# Python3 implementation of the above approach

# Function to return the word
# of the corresponding digit
def printValue(digit):

	# Switch block to check for each digit c

	# For digit 0
	if digit == '0':
		print("Zero ", end = " ")

	# For digit 1
	elif digit == '1':
		print("One ", end = " ")

	# For digit 2
	elif digit == '2':
		print("Two ", end = " ")

	#For digit 3
	elif digit=='3':
		print("Three",end=" ")

	# For digit 4
	elif digit == '4':
		print("Four ", end = " ")

	# For digit 5
	elif digit == '5':
		print("Five ", end = " ")

	# For digit 6
	elif digit == '6':
		print("Six ", end = " ")

	# For digit 7
	elif digit == '7':
		print("Seven", end = " ")

	# For digit 8
	elif digit == '8':
		print("Eight", end = " ")

	# For digit 9
	elif digit == '9':
		print("Nine", end =" ")

# Function to iterate through every
# digit in the given number
def printWord(N):
	i = 0
	length = len(N)

	# Finding each digit of the number
	while i < length:
		
		# Print the digit in words
		printValue(N[i])
		i += 1

# Driver code
N = input("enter a number: ")
printWord(N)

# This code is contributed by mohit kumar 29