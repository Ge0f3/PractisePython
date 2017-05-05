divisors=[]
numbers=range(1,100)
def finddiv(num):
	for element in numbers:
		if(num%element==0):
			divisors.append(element)
		else:
			continue
num=int(input("Enter a number to find its divisors :"))
finddiv(num)
print("The divisors for {} - {} ".format(num,divisors))

