def sumofnum(num):
	sumofn=0
	while num:
		sumofn=sumofn + num%10
		num=int(num/10)
	
	return sumofn
num=int(input("Enter the number for which you want to find the Sum : "))
sumofn=sumofnum(num)
print("The sum of {} is {}".format(num,sumofn))