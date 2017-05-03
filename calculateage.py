from datetime import date
name=str(input("Enter your name "))
age = int(input("Enter your age "))
if(age<100):
	print("{} you have {}years to turn 100 and, The year you will turn 100 is {} ".format(name,(100-age),(date.today().year+(100-age))))
else:
	print("{} you have crossed your 100th Birthday  ".format(name))

