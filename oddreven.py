def oddreven(num,divident,divisor):
	if(num%2==0):
		print("{} is even. ".format(num))
	else:
		print("{} is odd. ".format(num))
	if(num%4 == 0):
		print("4 is a divisor for {} .".format(num))
	try:
		if(divident%divisor==0):
			print("{} is evenly divided by {}.".format(divident,divisor))
	except :
		print("Opps the divident cannot be 0. ")

num=int(input("Enter a number "))
num1=int(input("Enter a number to divide "))
num2=int(input("Enter the divisor "))
oddreven(num,num1,num2)