import random
print("C'Mon lets play this Guessing Number game \n Instruction:The number will range from 0-9")
Num=random.randint(0,9)
guess=int(input("Enter your guess "))
count=1
print(Num)
while(Num!=guess):
	guess=int(input("It's not a correct guess one more time ? "))
	if(Num==guess):
		break
	else:
		count=count+1
print('Hurray you guessed it in {} guesses'.format(count))