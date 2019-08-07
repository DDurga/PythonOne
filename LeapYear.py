#in this Program the user will enter the Year and script will verify and give the Output as leap year or not
Year = int(input("enter a number:"))

if(Year%4==0 and Year%100!=0 or Year%400==0):
	print("{0} This is Leap Year".format(Year))
else:
	print("{0} This is not a Leap Year".format(Year))