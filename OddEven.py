#in this Program the user will enter the number and script will verify the odd or even
num = float(input("enter a number:"))
value= num % 2
if value > 0:
	print("This is an Odd number")
else:
	print("This is an Even number")