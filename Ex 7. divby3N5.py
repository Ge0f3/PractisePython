def sumofnum(num):
	sumofn=0
	while num:
		sumofn=sumofn + num%10
		num=int(num/10)
	
	return sumofn
num=int(input("Enter the number "))
sumofn=sumofnum(num)
if(sumofn%3==0 and num%10==0 or num%10==5):
	print("The num {} is divided by both 3 and 5".format(num))
elif(sumofn%3==0):
	print("The num {} is divided by 3".format(num))
elif(num%10==0 or num%10==5):
	print("The num {} is divided by 5".format(num))