import random
print("C'Mon lets play this Guessing Number game \n Instruction:The number will range from 0-9")
Num=random.randint(0,9)
guess=int(input("Enter your guess "))
count=1
while(Num!=guess):
	guess=int(input("It's not a correct wanna try or exit ? "))
	if(Num==guess):
		break
	elif(Num>guess):
		print("The number guessed is greather")
		count=count+1
	else:
		print("The numeber guessed is less")
		count=count+1		
print('Hurray {} it is !! and you guessed it in {} attempts'.format(Num,count))