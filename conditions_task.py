# Calculator contains the operations (+, -, *, /):

# asking the user to enter two numbers
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if (str(num1).isdigit()) and (str(num2).isdigit()) :
	# the inputs are numbers 

	# now we need to ask the user to choose an operation
	operation = input ("Choose the operation (+, -, /, *): ")

	if operation == "+" :
		print ("The answer is", int(num1)+int(num2))

	elif operation == "-" :
		print ("The answer is", int(num1)-int(num2))

	elif operation == "/" :
		print ("The answer is", float(num1)/float(num2))

	elif operation == "*" :
		print ("The answer is", int(num1)*int(num2))

	else :
		print ("The operation is not valid !!!")

else :
	# the inputs are not numbers !!!
	print ("Sorry! The numbers are invalid!!")
